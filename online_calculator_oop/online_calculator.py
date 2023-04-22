from typing import List
import operator as operation


class OnlineCalculator:
    VALID_OPERATORS_LIST: List[str] = ["+", "-", "*", "/"]

    def __init__(self, operator: str, first_number: int or float, second_number: int or float):
        self.operator = operator
        self.first_number = first_number
        self.second_number = second_number
        self.result: None or int or float = None

    @property   # getter
    def operator(self) -> str:
        return self.__operator

    @operator.setter   # setter
    def operator(self, value: str) -> [None, ValueError]:
        if value in self.VALID_OPERATORS_LIST:
            self.__operator = value
        else:
            raise ValueError("Invalid operator. Try again...")

    @property   # getter
    def first_number(self) -> int or float:
        return self.__first_number

    @first_number.setter   # setter
    def first_number(self, value: int or float) -> [None, ValueError]:
        if isinstance(value, (int, float)):
            self.__first_number = value
        else:
            raise ValueError("Invalid number. Try again...")

    @property  # getter
    def second_number(self) -> int or float:
        return self.__second_number

    @second_number.setter  # setter
    def second_number(self, value: int or float) -> [ZeroDivisionError, None, ValueError]:
        if isinstance(value, (int, float)):
            if self.operator == "/" and value == 0:
                raise ZeroDivisionError("Invalid operation! Can't divide by zero!")

            else:
                self.__second_number = value

        else:
            raise ValueError("Invalid number. Try again...")

    def __add(self) -> [int, float]:
        return operation.add(self.first_number, self.second_number)

    def __subtract(self) -> [int, float]:
        return operation.sub(self.first_number, self.second_number)

    def __multiply(self) -> [int, float]:
        return operation.mul(self.first_number, self.second_number)

    def __divide(self) -> [int, float]:
        return operation.truediv(self.first_number, self.second_number)

    def calculating(self) -> None:
        if self.operator == "+":
            self.result = self.__add()

        elif self.operator == "-":
            self.result = self.__subtract()

        elif self.operator == "*":
            self.result = self.__multiply()

        elif self.operator == "/":
            self.result = self.__divide()

    def __repr__(self) -> str:
        if self.result is not None:
            first_number = self.first_number
            operator = self.operator
            second_number = self.second_number if self.second_number >= 0 else f"({self.second_number})"
            result = self.result

            return f"Calculation: {first_number} {operator} {second_number} = {result}" \
                   f"\nResult: {result}"

        else:
            return "First you have to calculating!"


# print("""
#                 WELCOME TO MY
#              "ONLINE CALCULATOR"
#
# """)
#
#
# def valid_operator_function(value: str):
#     operators_dict = {"+": "+", "add": "+",
#                       "-": "-", "subtract": "-",
#                       "*": "*", "multiply": "*",
#                       "/": "/", "divide": "/"}
#     if value.lower() in operators_dict.keys():
#         valid_value = operators_dict[value.lower()]
#         return valid_value
#     else:
#         raise SystemExit("Invalid operator. Try again...")
#
#
# def valid_number_function(value: str):
#     try:
#         if "." in value:
#             valid_value = float(value)
#         elif "," in value:
#             edit_value = value.replace(",", ".")
#             valid_value = float(edit_value)
#         else:
#             valid_value = int(value)
#         return valid_value
#     except ValueError:
#         raise SystemExit("Invalid number. Try again...")
#
#
# current_operator = input("""Operator options:
# [+] Add
# [-] Subtract
# [*] Multiply
# [/] Divide
#
# Choose operator: """)
# valid_operator = valid_operator_function(current_operator)
#
# current_first_number = input("Enter first number: ")
# valid_first_number = valid_number_function(current_first_number)
#
# current_second_number = input("Enter second number: ")
# valid_second_number = valid_number_function(current_second_number)
# print("\n")
#
#
# online_calculator_object = OnlineCalculator(valid_operator, valid_first_number, valid_second_number)
# online_calculator_object.calculating()
# print(online_calculator_object.__repr__())
#
#
# print("""
#
#              THANK YOU FOR USING MY
#                ONLINE CALCULATOR!
# """)
