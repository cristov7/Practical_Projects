def return_result_from_decimal_number_system_function(current_number: str):
    calculation_list = []
    digit = int(current_number)
    while True:
        if digit == 0:
            break
        else:
            remainder = digit % 2
            calculation_list.append(remainder)
            digit //= 2
    calculation_list.reverse()
    calculation = "".join([str(element) for element in calculation_list])
    return calculation


def return_result_from_hexadecimal_number_system_function(current_number: str):
    calculation = ""
    digits_list = list(current_number)
    convert_to_digits_dict = {
        "0": "0000", "1": "0001", "2": "0010", "3": "0011",
        "4": "0100", "5": "0101", "6": "0110", "7": "0111",
        "8": "1000", "9": "1001", "A": "1010", "B": "1011",
        "C": "1100", "D": "1101", "E": "1110", "F": "1111"}
    for digit in digits_list:
        value = convert_to_digits_dict[digit]
        calculation += value
    return calculation


print("""
        Convert to binary number system:
""")
while True:
    number = input("\nEnter number: ")
    choose = input("\nOptions:"
                   "\n- from the decimal number system:       [10]"
                   "\n- from the hexadecimal number system:   [16]"
                   "\nChoose: ")
    if choose == "10" and number.isdigit():
        result = return_result_from_decimal_number_system_function(number)
        print(f"\n{number}(10) = {result}(2)")
    elif choose == "16":
        result = return_result_from_hexadecimal_number_system_function(number)
        print(f"\n{number}(16) = {result}(2)")
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
