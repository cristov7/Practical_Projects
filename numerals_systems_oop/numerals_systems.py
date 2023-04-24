from typing import Dict
from collections import deque


class NumeralsSystems:
    NUMERALS_SYSTEMS_DICT: Dict[str, str] = {"1": ["From Decimal to Binary numeral system", 10, 2],
                                             "2": ["From Hexadecimal to Binary numeral system", 16, 2],
                                             "3": ["From Binary to Decimal numeral system", 2, 10],
                                             "4": ["From Hexadecimal to Decimal numeral system", 16, 10],
                                             "5": ["From Binary to Hexadecimal numeral system", 2, 16],
                                             "6": ["From Decimal to Hexadecimal numeral system", 10, 16]}

    def __init__(self, option: str, number: int or str):
        self.option = option
        self.number = number
        self.convert_number: None or int or str = None

    @property   # getter
    def option(self) -> str:
        return self.__option

    @option.setter   # setter
    def option(self, value: str) -> [None, ValueError]:
        if value in self.NUMERALS_SYSTEMS_DICT.keys():
            self.__option = value
        else:
            raise ValueError("Invalid numeral system! Try again...")

    @property   # getter
    def number(self) -> int or str:
        return self.__number

    @number.setter   # setter
    def number(self, value: int or str) -> [None, ValueError]:
        allow_letters_list = ["A", "B", "C", "D", "E", "F"]
        allow_digits_list = ["0", "1"]

        if (self.option == "1" or self.option == "6") and isinstance(value, int):
            self.__number = value

        elif (self.option == "2" or self.option == "4") and isinstance(value, str):
            for char in value:
                if not char.isdigit() and char not in allow_letters_list:
                    raise ValueError("Invalid number! Try again...")

            self.__number = value

        elif (self.option == "3" or self.option == "5") and isinstance(value, str):
            for char in value:
                if char not in allow_digits_list:
                    raise ValueError("Invalid number! Try again...")

            self.__number = value

        else:
            raise ValueError("Invalid number! Try again...")

    def set_convert_number(self) -> None:
        if self.option == "1":
            self.__calculate_from_decimal_to_binary_numeral_system()

        elif self.option == "2":
            self.__calculate_from_hexadecimal_to_binary_numeral_system()

        elif self.option == "3":
            self.__calculate_from_binary_to_decimal_numeral_system()

        elif self.option == "4":
            self.__calculate_from_hexadecimal_to_decimal_numeral_system()

        elif self.option == "5":
            self.__calculate_from_binary_to_hexadecimal_numeral_system()

        elif self.option == "6":
            self.__calculate_from_decimal_to_hexadecimal_numeral_system()

    def __calculate_from_decimal_to_binary_numeral_system(self) -> None:
        calculation_list = []
        digit = self.number

        while digit != 0:
            remainder = digit % 2
            calculation_list.append(remainder)
            digit //= 2

        calculation_list.reverse()
        calculation = "".join([str(element) for element in calculation_list])

        self.convert_number = calculation

    def __calculate_from_hexadecimal_to_binary_numeral_system(self) -> None:
        calculation = ""
        convert_to_digits_dict = {
            "0": "0000", "1": "0001", "2": "0010", "3": "0011",
            "4": "0100", "5": "0101", "6": "0110", "7": "0111",
            "8": "1000", "9": "1001", "A": "1010", "B": "1011",
            "C": "1100", "D": "1101", "E": "1110", "F": "1111"}
        digits_list = list(self.number)

        for digit in digits_list:
            value = convert_to_digits_dict[digit]
            calculation += value

        self.convert_number = calculation

    def __calculate_from_binary_to_decimal_numeral_system(self) -> None:
        calculation = 0
        digits_list = list(self.number)
        degree = len(digits_list) - 1

        for digit in digits_list:
            calculation += (int(digit) * 2 ** degree)
            degree -= 1

        self.convert_number = calculation

    def __calculate_from_hexadecimal_to_decimal_numeral_system(self) -> None:
        calculation = 0
        convert_letters_to_digits_dict = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}
        digits_list = list(self.number)
        degree = len(digits_list) - 1

        for digit in digits_list:
            if digit in convert_letters_to_digits_dict.keys():
                digit = convert_letters_to_digits_dict[digit]
                calculation += (digit * 16 ** degree)
                degree -= 1

            else:
                calculation += (int(digit) * 16 ** degree)
                degree -= 1

        self.convert_number = calculation

    def __calculate_from_binary_to_hexadecimal_numeral_system(self) -> None:
        calculation = ""
        convert_to_digits_dict = {
            "0000": "0", "0001": "1", "0010": "2", "0011": "3",
            "0100": "4", "0101": "5", "0110": "6", "0111": "7",
            "1000": "8", "1001": "9", "1010": "A", "1011": "B",
            "1100": "C", "1101": "D", "1110": "E", "1111": "F"}

        number = self.number

        if len(number) % 4 == 1:
            number = "000" + number

        elif len(number) % 4 == 2:
            number = "00" + number

        elif len(number) % 4 == 3:
            number = "0" + number

        numbers_queue = deque(number)
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
            self.convert_number = calculation
        else:
            self.convert_number = "0"

    def __calculate_from_decimal_to_hexadecimal_numeral_system(self) -> None:
        calculation_list = []
        convert_to_digits_dict = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
        digit = self.number

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

        self.convert_number = calculation

    def __repr__(self) -> str:
        if self.convert_number is not None:

            option_text = self.NUMERALS_SYSTEMS_DICT[self.option][0]
            from_numeral_system = self.NUMERALS_SYSTEMS_DICT[self.option][1]
            to_numeral_system = self.NUMERALS_SYSTEMS_DICT[self.option][2]

            return f"{option_text}:" \
                   f"\n{self.number}({from_numeral_system}) = {self.convert_number}({to_numeral_system})"

        else:
            return "First you have to set convert number!"


# print("""
#                    Numerals Systems:
#             Binary, Decimal and Hexadecimal
#
# """)
#
#
# def valid_option_function(value: str):
#     options_dict = {"1": "from decimal to binary numeral system",
#                     "2": "from hexadecimal to binary numeral system",
#                     "3": "from binary to decimal numeral system",
#                     "4": "from hexadecimal to decimal numeral system",
#                     "5": "from binary to hexadecimal numeral system",
#                     "6": "from decimal to hexadecimal numeral system"}
#
#     if value in options_dict.keys():
#         return [value, options_dict[value]]
#
#     else:
#         raise SystemExit("Invalid numeral system! Try again...")
#
#
# def valid_number_function(option: str, value: str):
#     allow_letters_list = ["A", "B", "C", "D", "E", "F"]
#     allow_digits_list = ["0", "1"]
#
#     try:
#         if option == "1" or option == "6":
#             value = int(value)
#
#         elif option == "2" or option == "4":
#             for char in value:
#                 if not char.isdigit() and char not in allow_letters_list:
#                     raise ValueError("Invalid number! Try again...")
#
#         elif option == "3" or option == "5":
#             for char in value:
#                 if char not in allow_digits_list:
#                     raise ValueError("Invalid number! Try again...")
#
#         return value
#
#     except ValueError:
#         raise ValueError("Invalid number! Try again...")
#
#
# current_option = input("\nNumerals systems options:"
#
#                        "\n- from decimal to binary numeral system:        [1]"
#                        "\n- from hexadecimal to binary numeral system:    [2]"
#
#                        "\n- from binary to decimal numeral system:        [3]"
#                        "\n- from hexadecimal to decimal numeral system:   [4]"
#
#                        "\n- from binary to hexadecimal numeral system:    [5]"
#                        "\n- from decimal to hexadecimal numeral system:   [6]"
#
#                        "\n\nChoose numeral system: ")
# valid_options_list = valid_option_function(current_option)
#
# valid_option = valid_options_list[0]
# valid_option_text = valid_options_list[1]
#
#
# current_number = input(f"Enter number {valid_option_text}: ")
# valid_number = valid_number_function(valid_option, current_number)
# print("\n")
#
#
# numerals_systems_object = NumeralsSystems(valid_option, valid_number)
# numerals_systems_object.set_convert_number()
# print(numerals_systems_object.__repr__())
#
#
# print("""
#
#     Thank you for using my numerals systems program!
# """)
