# import math


def return_factorial_of_number(number: int):
    calculation = number
    for multiply in range(number - 1, 0, - 1):
        calculation *= multiply
    return calculation


print("""

            Factorials Calculator:

""")
yes_list = ["Y", "YES"]
no_list = ["N", "NO"]
while True:
    try:
        current_number = int(input("Enter number: "))
        # factorial_of_number = math.factorial(number)
        factorial_of_number = return_factorial_of_number(current_number)
        print(f"Factorial: {factorial_of_number}\n\n")
        info = input("Do you want to try again?"
                     "\nOptions:"
                     "\n - Yes -> [Y]"
                     "\n - No  -> [N]"
                     "\nChoose: ")
        if info.upper() in yes_list:
            print()
            print()
        elif info.upper() in no_list:
            print("\n\n      Thank you for using my calculator!\n\n")
            raise SystemExit
        else:
            print("\n\nInvalid option!"
                  "\nThe program was stopped!\n\n")
            raise SystemExit
    except ValueError:
        print("\n\nThe number must be an integer!"
              "\nPlease, try again!\n\n")
