import math


class FactorialCalculator:
    def __init__(self, number: int):
        self.number = number
        self.factorial_of_number: None or int = None

    @property   # getter
    def number(self) -> int:
        return self.__number

    @number.setter   # setter
    def number(self, value: int) -> [None, ValueError]:
        if isinstance(value, int):
            self.__number = value
        else:
            raise ValueError("The number must be an integer!")

    def calculate_factorial_of_number(self) -> None:
        self.factorial_of_number = math.factorial(self.number)

    def __repr__(self) -> str:
        if self.factorial_of_number is not None:
            calculation_info = f"{self.number}! = "

            if self.number == 0:
                calculation_info += "1"

            elif self.number == 1:
                calculation_info += "1"

            else:
                for number in range(self.number, 0, - 1):
                    if number > 1:
                        calculation_info += f"{number} x "

                    else:
                        calculation_info += f"{number} = {self.factorial_of_number}"

            output = f"Factorial function:" \
                     f"\n{calculation_info}" \
                     f"\nResult: {self.factorial_of_number}"
            return output

        else:
            return "First you have to calculate factorial of number!"


# print("""
#                 Welcome to my:
#             !Factorial Calculator!
#
# """)
#
#
# current_number = int(input("Enter number: "))
# print("\n")
#
#
# factorial_calculator_object = FactorialCalculator(current_number)
# factorial_calculator_object.calculate_factorial_of_number()
# print(factorial_calculator_object.__repr__())
#
#
# print("""
#
#            Thanks you for using my:
#            !Factorials Calculator!
# """)
