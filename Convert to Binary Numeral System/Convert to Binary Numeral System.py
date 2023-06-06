def calculate_from_decimal_numeral_system_function(current_number: str):
    calculation_list = []

    digit = int(current_number)

    while digit != 0:
        remainder = digit % 2
        calculation_list.append(remainder)
        digit //= 2

    calculation_list.reverse()
    calculation = "".join([str(element) for element in calculation_list])

    return calculation


def calculate_from_hexadecimal_numeral_system_function(current_number: str):
    calculation = ""
    convert_to_digits_dict = {
        "0": "0000", "1": "0001", "2": "0010", "3": "0011",
        "4": "0100", "5": "0101", "6": "0110", "7": "0111",
        "8": "1000", "9": "1001", "A": "1010", "B": "1011",
        "C": "1100", "D": "1101", "E": "1110", "F": "1111"}

    digits_list = list(current_number)

    for digit in digits_list:
        value = convert_to_digits_dict[digit]
        calculation += value

    return calculation


print("""
             Convert to:      
        Binary Numeral System  
           
""")


yes_list = ["yes", "y"]
no_list = ["no", "n"]

while True:
    number = input("Enter number: ")
    choose = input("\nOptions:"
                   "\n- from decimal to binary numeral system:       [10]"
                   "\n- from hexadecimal to binary numeral system:   [16]"
                   "\nChoose: ")

    if choose == "10" and number.isdigit():
        result = calculate_from_decimal_numeral_system_function(number)
        print(f"\n{number}(10) = {result}(2)")

    elif choose == "16" and all([True if char.isdigit() or char in "ABCDEF"
                                 else False
                                 for char in number]):

        result = calculate_from_hexadecimal_numeral_system_function(number)
        print(f"\n{number}(16) = {result}(2)")

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
