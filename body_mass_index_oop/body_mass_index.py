# import re


class BodyMassIndex:
    def __init__(self, weight: float, height: float):
        self.weight = weight
        self.height = height
        self.body_mass_index: None or int = None

    @property   # getter
    def weight(self) -> float:
        return self.__weight

    @weight.setter   # setter
    def weight(self, value: float) -> [None, ValueError]:
        if 0.00 < value <= 300.00:
            self.__weight = value
        else:
            raise ValueError("Invalid weight. Try again in kg...")

    @property   # getter
    def height(self) -> float:
        return self.__height

    @height.setter   # setter
    def height(self, value: float) -> [None, ValueError]:
        if 0.00 < value <= 300.00:
            self.__height = value
        else:
            raise ValueError("Invalid height. Try again in cm...")

    def calculate_body_mass_index(self) -> None:
        calculation = self.weight / (self.height / 100) ** 2
        if calculation <= 24.9:
            self.body_mass_index = 0
        elif calculation <= 29.9:
            self.body_mass_index = 1
        elif calculation <= 39.9:
            self.body_mass_index = 2
        else:
            self.body_mass_index = 3

    def __repr__(self) -> str:
        if self.body_mass_index is None:
            return "First you have to calculate body mass index!"
        else:
            body_mass_index = self.body_mass_index
            return f"{body_mass_index}th degree of obesity."


# print("""
#               Welcome to my
#             "Body Mass Index"
#
# """)
#
#
# def validator(value: str):
#     regex_int = r"^(\d+)$"
#     match = re.search(regex_int, value)
#     if match:
#         valid_value = float(match.group(1))
#         return valid_value
#
#     regex_float_point = r"^(\d{1,}\.{1}\d{1,})$"
#     match = re.search(regex_float_point, value)
#     if match:
#         valid_value = float(match.group(1))
#         return valid_value
#
#     regex_float_comma = r"^(\d{1,}\,{1}\d{1,})$"
#     match = re.search(regex_float_comma, value)
#     if match:
#         current_value = match.group(1)
#         edit_current_value = current_value.replace(",", ".")
#         valid_value = float(edit_current_value)
#         return valid_value
#
#     else:
#         raise SystemExit("Invalid value! Please try again!")
#
#
# kg = input("Enter your weigh in kg: ")
# valid_kg = validator(kg)
#
# cm = input("Enter your height in cm: ")
# valid_cm = validator(cm)
#
# body_mass_index_object = BodyMassIndex(valid_kg, valid_cm)
# body_mass_index_object.calculate_body_mass_index()
# output = body_mass_index_object.__repr__()
#
# print(f"\nBody Mass Index:"
#       f"\n{output}")
#
#
# print("""
#
#           THANK YOU FOR USING MY
#             "BODY MASS INDEX!"
# """)
