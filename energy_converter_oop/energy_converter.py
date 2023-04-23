# import re
from typing import Dict


class EnergyConverter:
    ENERGY_DICT: Dict[str, float] = {"from kcal to kJ": 4.18,
                                     "from kJ to kcal": 0.24}

    def __init__(self, option: str, energy: float):
        self.option = option
        self.energy = energy
        self.convert_energy: None or float = None

    @property   # getter
    def energy(self) -> float:
        return self.__energy

    @energy.setter   # setter
    def energy(self, value: float) -> [None, ValueError]:
        if 0.00 < value:
            self.__energy = value
        else:
            raise ValueError("Invalid energy. Try again...")

    def __converter_from_kcal_to_kj(self) -> float:
        return self.energy * self.ENERGY_DICT["from kcal to kJ"]

    def __converter_from_kj_to_kcal(self) -> float:
        return self.energy * self.ENERGY_DICT["from kJ to kcal"]

    def calculate_convert_energy(self) -> None:
        if self.option == "from kcal to kJ":
            self.convert_energy = self.__converter_from_kcal_to_kj()

        elif self.option == "from kJ to kcal":
            self.convert_energy = self.__converter_from_kj_to_kcal()

    def __repr__(self) -> str:
        if self.convert_energy is not None:
            output_list = [f"Converting {self.option}:"]

            if self.option == "from kcal to kJ":
                kcal = self.energy
                kj = self.convert_energy
                convert_info = f"{kcal} kcal = {kj:.2f} kJ"
                output_list.append(convert_info)

            elif self.option == "from kJ to kcal":
                kj = self.energy
                kcal = self.convert_energy
                convert_info = f"{kj} kJ = {kcal:.2f} kcal"
                output_list.append(convert_info)

            output = "\n".join(output_list)
            return output

        else:
            return "First you have to calculate convert energy!"


# print("""
#               WELCOME TO MY
#             "ENERGY CONVERTER"
#
# """)
#
#
# def valid_option_function(value: str):
#     if value == "1" or value.lower() == "from kcal to kj":
#         return "from kcal to kJ"
#
#     elif value == "2" or value.lower() == "from kj to kcal":
#         return "from kJ to kcal"
#
#     else:
#         raise SystemExit("Invalid choice. Try again...")
#
#
# def valid_energy_function(value: str):
#     regex_plus_int = r"^(\d+)$"
#     match = re.search(regex_plus_int, value)
#     if match:
#         valid_value = float(match.group(1))
#         return valid_value
#
#     regex_plus_float_point = r"^(\d{1,}\.{1}\d{1,})$"
#     match = re.search(regex_plus_float_point, value)
#     if match:
#         valid_value = float(match.group(1))
#         return valid_value
#
#     regex_plus_float_comma = r"^(\d{1,}\,{1}\d{1,})$"
#     match = re.search(regex_plus_float_comma, value)
#     if match:
#         current_value = match.group(1)
#         edit_current_value = current_value.replace(",", ".")
#         valid_value = float(edit_current_value)
#         return valid_value
#
#     else:
#         raise SystemExit("Invalid value. Try again...")
#
#
# current_option = input("""Converter options:
# [1] - from kcal to kJ
# [2] - from kJ to kcal
#
# Choose converter: """)
# valid_option = valid_option_function(current_option)
#
#
# current_energy = ""
#
# if valid_option == "from kcal to kJ":
#     current_energy = input("Enter kcal: ")
#
# elif valid_option == "from kJ to kcal":
#     current_energy = input("Enter kJ: ")
#
# valid_energy = valid_energy_function(current_energy)
# print("\n")
#
#
# energy_convertor_object = EnergyConverter(valid_option, valid_energy)
# energy_convertor_object.calculate_convert_energy()
# print(energy_convertor_object.__repr__())
#
#
# print("""
#
#             THANK YOU FOR USING MY
#               !ENERGY CONVERTER!
# """)
