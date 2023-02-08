from collections import deque


def return_result_from_binary_number_system_function(current_number: str):
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
    return calculation


def return_result_from_decimal_number_system_function(current_number: str):
    calculation_list = []
    convert_to_digits_dict = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
    digit = int(current_number)
    while True:
        if digit == 0:
            break
        else:
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
        Convert to hexadecimal number system:
""")
while True:
    number = input("\nEnter number: ")
    choose = input("\nOptions:"
                   "\n- from the binary number system:    [2]"
                   "\n- from the decimal number system:   [10]"
                   "\nChoose: ")
    if choose == "2" and number.isdigit():
        result = return_result_from_binary_number_system_function(number)
        print(f"\n{number}(2) = {result}(16)")
    elif choose == "10" and number.isdigit():
        result = return_result_from_decimal_number_system_function(number)
        print(f"\n{number}(10) = {result}(16)")
    else:
        print("\n\nInvalid number system!")
    again = input("\n\nDo you want to try again?"
                  "\nOptions:"
                  "\n- Yes:   [Y]"
                  "\n- No:    [N]"
                  "\nChoose: ")
    yes_list = ["yes", "y"]
    no_list = ["no", "n"]
    if again.lower() in yes_list:
        print()
        continue
    elif again.lower() in no_list:
        print("\n\nThanks for using my program!")
        break
    else:
        print("Invalid options!")
        break
