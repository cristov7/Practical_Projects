from collections import deque


def calculate_from_binary_numeral_system_function(current_number: str):
    calculation = ""
    convert_to_digits_dict = {
        "0000": "0", "0001": "1", "0010": "2", "0011": "3",
        "0100": "4", "0101": "5", "0110": "6", "0111": "7",
        "1000": "8", "1001": "9", "1010": "A", "1011": "B",
        "1100": "C", "1101": "D", "1110": "E", "1111": "F"}

    if len(current_number) % 4 == 1:
        current_number = "000" + current_number

    elif len(current_number) % 4 == 2:
        current_number = "00" + current_number

    elif len(current_number) % 4 == 3:
        current_number = "0" + current_number

    numbers_queue = deque(current_number)
    while numbers_queue:

        first_digit = numbers_queue.popleft()
        second_digit = numbers_queue.popleft()
        third_digit = numbers_queue.popleft()
        fourth_digit = numbers_queue.popleft()

        digit = first_digit + second_digit + third_digit + fourth_digit

        value = convert_to_digits_dict[digit]
        calculation += value

    calculation = calculation.lstrip("0")

    if calculation:
        return calculation
    else:
        return "0"


def calculate_from_decimal_numeral_system_function(current_number: str):
    calculation_list = []
    convert_to_digits_dict = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}

    digit = int(current_number)

    while digit != 0:
        remainder = digit % 16

        if remainder > 9:
            remainder = convert_to_digits_dict[remainder]
            calculation_list.append(remainder)
            digit //= 16

        else:
            calculation_list.append(remainder)
            digit //= 16

    calculation_list.reverse()
    calculation = "".join([str(element) for element in calculation_list])

    return calculation


print("""
             Convert to:      
        Hexadecimal Numeral System  

""")


yes_list = ["yes", "y"]
no_list = ["no", "n"]

while True:
    number = input("Enter number: ")
    choose = input("\nOptions:"
                   "\n- from binary to hexadecimal number system:    [2]"
                   "\n- from decimal to hexadecimal number system:   [10]"
                   "\nChoose: ")

    if choose == "2" and all([True if char in "01" else False
                              for char in number]):

        result = calculate_from_binary_numeral_system_function(number)
        print(f"\n{number}(2) = {result}(16)")

    elif choose == "10" and number.isdigit():
        result = calculate_from_decimal_numeral_system_function(number)
        print(f"\n{number}(10) = {result}(16)")

    else:
        raise SystemExit("Invalid numeral system! Try again...")

    again = input("\n\nDo you want to try again?"
                  "\nOptions:"
                  "\n- Yes:   [Y]"
                  "\n- No:    [N]"
                  "\nChoose: ")

    if again.lower() in yes_list:
        print("\n")
        continue

    elif again.lower() in no_list:
        print("\n\n   Thank you for using my program!")
        break

    else:
        raise SystemExit("Invalid option!")
