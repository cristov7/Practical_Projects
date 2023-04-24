def calculate_from_binary_numeral_system_function(current_number: str):
    calculation = 0

    digits_list = list(current_number)
    degree = len(digits_list) - 1

    for digit in digits_list:
        calculation += (int(digit) * 2 ** degree)
        degree -= 1

    return calculation


def calculate_from_hexadecimal_numeral_system_function(current_number: str):
    calculation = 0
    convert_letters_to_digits_dict = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}

    digits_list = list(current_number)
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
             Convert to:      
        Decimal Numeral System  

""")


yes_list = ["yes", "y"]
no_list = ["no", "n"]

while True:
    number = input("Enter number: ")
    choose = input("\nOptions:"
                   "\n- from binary to decimal numeral system:        [2]"
                   "\n- from hexadecimal to decimal numeral system:   [16]"
                   "\nChoose: ")

    if choose == "2" and all([True if char in "01" else False
                              for char in number]):

        result = calculate_from_binary_numeral_system_function(number)
        print(f"\n{number}(2) = {result}(10)")

    elif choose == "16" and all([True if char.isdigit() or char in "ABCDEF"
                                 else False
                                 for char in number]):

        result = calculate_from_hexadecimal_numeral_system_function(number)
        print(f"\n{number}(16) = {result}(10)")

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
