def return_result_from_binary_number_system_function(current_number: str):
    calculation = 0
    digits_list = list(current_number)
    degree = len(digits_list) - 1
    for digit in digits_list:
        calculation += (int(digit) * 2 ** degree)
        degree -= 1
    return calculation


def return_result_from_hexadecimal_number_system_function(current_number: str):
    calculation = 0
    digits_list = list(current_number)
    convert_letters_to_digits_dict = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}
    degree = len(digits_list) - 1
    for digit in digits_list:
        if digit in convert_letters_to_digits_dict.keys():
            digit = convert_letters_to_digits_dict[digit]
            calculation += (digit * 16 ** degree)
            degree -= 1
        else:
            calculation += (int(digit) * 16 ** degree)
            degree -= 1
    return calculation


print("""
        Convert to decimal number system:
""")
while True:
    number = input("\nEnter number: ")
    choose = input("\nOptions:"
                   "\n- from the binary number system:        [2]"
                   "\n- from the hexadecimal number system:   [16]"
                   "\nChoose: ")
    if choose == "2" and number.isalpha():
        result = return_result_from_binary_number_system_function(number)
        print(f"\n{number}(2) = {result}(10)")
    elif choose == "16":
        result = return_result_from_hexadecimal_number_system_function(number)
        print(f"\n{number}(16) = {result}(10)")
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
