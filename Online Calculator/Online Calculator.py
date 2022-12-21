import re
print("""
                WELCOME TO MY
             "ONLINE CALCULATOR"

""")


def valid_operator_function(current_operator: str):
    operators_dict = {"+": "+", "add": "+", "Add": "+", "ADD": "+",
                      "-": "-", "subtract": "-", "Subtract": "-", "SUBTRACT": "-",
                      "*": "*", "multiply": "*", "Multiply": "*", "MULTIPLY": "*",
                      "/": "/", "divide": "/", "Divide": "/", "DIVIDE": "/"}
    if current_operator in operators_dict:
        valid_current_operator = operators_dict[current_operator]
        return valid_current_operator
    else:
        raise SystemExit("Invalid operator. Try again...")


def valid_number_function(current_number: str):
    # if current_number.isdigit():
    #     return int(current_number)
    regex_plus_int = r"^(\d+)$"
    match = re.search(regex_plus_int, current_number)
    if match:
        valid_current_number = int(match.group(1))
        return valid_current_number
    regex_minus_int = r"^(\-\d+)$"
    match = re.search(regex_minus_int, current_number)
    if match:
        valid_current_number = int(match.group(1))
        return valid_current_number
    regex_plus_float_point = r"^(\d{1,}\.{1}\d{1,})$"
    match = re.search(regex_plus_float_point, current_number)
    if match:
        valid_current_number = float(match.group(1))
        return valid_current_number
    regex_minus_float_point = r"^(\-{1}\d{1,}\.{1}\d{1,})$"
    match = re.search(regex_minus_float_point, current_number)
    if match:
        valid_current_number = float(match.group(1))
        return valid_current_number
    regex_plus_float_comma = r"^(\d{1,}\,{1}\d{1,})$"
    match = re.search(regex_plus_float_comma, current_number)
    if match:
        current_match = match.group(1)
        current_number_as_string = current_match.replace(",", ".")
        valid_current_number = float(current_number_as_string)
        return valid_current_number
    regex_minus_float_comma = r"^(\-{1}\d{1,}\,{1}\d{1,})$"
    match = re.search(regex_minus_float_comma, current_number)
    if match:
        current_match = match.group(1)
        current_number_as_string = current_match.replace(",", ".")
        valid_current_number = float(current_number_as_string)
        return valid_current_number
    else:
        raise SystemExit("Invalid number. Try again...")


def calculating_function(operation: str, number_1, number_2):
    if operation == "+":
        number = number_1 + number_2
        if number_1 < 0:
            number_1 = f"({number_1})"
        if number_2 < 0:
            number_2 = f"({number_2})"
        result = f"\n{number_1} {operation} {number_2} = {number:.2f}"
        return result
    elif operation == "-":
        number = number_1 - number_2
        if number_1 < 0:
            number_1 = f"({number_1})"
        if number_2 < 0:
            number_2 = f"({number_2})"
        result = f"\n{number_1} {operation} {number_2} = {number:.2f}"
        return result
    elif operation == "*":
        number = number_1 * number_2
        if number_1 < 0:
            number_1 = f"({number_1})"
        if number_2 < 0:
            number_2 = f"({number_2})"
        result = f"\n{number_1} {operation} {number_2} = {number:.2f}"
        return result
    elif operation == "/":
        if number_2 != 0:
            number = number_1 / number_2
            if number_1 < 0:
                number_1 = f"({number_1})"
            if number_2 < 0:
                number_2 = f"({number_2})"
            result = f"\n{number_1} {operation} {number_2} = {number:.2f}"
            return result
        else:
            raise SystemExit("Invalid operation. You can't divide by zero. Try again...")


while True:
    operator = input("""Operators: 
    [+] add
    [-] subtract
    [*] multiply
    [/] divide
    Choose operator: """)
    print()
    valid_operator = valid_operator_function(operator)
    first_number = input("Enter first number: ")
    valid_first_number = valid_number_function(first_number)
    second_number = input("Enter second number: ")
    valid_second_number = valid_number_function(second_number)
    calculating = calculating_function(valid_operator, valid_first_number, valid_second_number)
    print(f"{calculating}\n\n")
    command = input("Click [Enter] to calculating again.\n\n")
    if command == "":
        continue
    else:
        print("""             THANK YOU FOR USING MY
               ONLINE CALCULATOR!
        """)
        break
