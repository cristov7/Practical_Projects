# import re
from typing import Dict
from calculate_macronutrients_oop.protein import Protein
from calculate_macronutrients_oop.fat import Fat
from calculate_macronutrients_oop.carb import Carb


class CalculateMacronutrients:
    PERCENTS_DICT: Dict[str, int] = {"Protein": Protein.PERCENT,
                                     "Fat": Fat.PERCENT,
                                     "Carb": Carb.PERCENT}

    def __init__(self, daily_target_kcal: float):
        self.daily_target_kcal = daily_target_kcal
        self.protein_kcal: None or float = None
        self.fat_kcal: None or float = None
        self.carb_kcal: None or float = None

    @property   # getter
    def daily_target_kcal(self) -> float:
        return self.__daily_target_kcal

    @daily_target_kcal.setter   # setter
    def daily_target_kcal(self, value: float) -> [None, ValueError]:
        if 0.00 < value:
            self.__daily_target_kcal = value
        else:
            raise ValueError("Invalid kcal! Try again...")

    def __calculate_protein_kcal(self) -> None:   # private method
        percents = (self.PERCENTS_DICT["Protein"] / 100)
        self.protein_kcal = self.daily_target_kcal * percents

    def __calculate_fat_kcal(self) -> None:   # private method
        percents = (self.PERCENTS_DICT["Fat"] / 100)
        self.fat_kcal = self.daily_target_kcal * percents

    def __calculate_carb_kcal(self) -> None:   # private method
        percents = (self.PERCENTS_DICT["Carb"] / 100)
        self.carb_kcal = self.daily_target_kcal * percents

    def calculate_macronutrients(self) -> None:
        self.__calculate_protein_kcal()
        self.__calculate_fat_kcal()
        self.__calculate_carb_kcal()

    def __repr__(self) -> str:
        output_list = []

        for macronutrient, percent in self.PERCENTS_DICT.items():
            macronutrient_info = f"{macronutrient} {percent} %"

            if macronutrient == "Protein":
                macronutrient_info += f" -> {self.protein_kcal:.2f} kcal"

            elif macronutrient == "Fat":
                macronutrient_info += f" -> {self.fat_kcal:.2f} kcal"

            elif macronutrient == "Carb":
                macronutrient_info += f" -> {self.carb_kcal:.2f} kcal"

            output_list.append(macronutrient_info)

        output_list.extend([f"\n({Protein().details()})",
                            f"({Fat().details()})",
                            f"({Carb().details()})"])

        output = "\n".join(output_list)
        return output


# print("""
#               Healthy Eating
#          Calculate Macronutrients
#            "Protein, Fat, Carb"
#
# """)
#
#
# def valid_daily_energy_consumption_function(value: str):
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
# daily_energy_consumption = input("Enter your kcal (target for 1 day): ")
# valid_daily_energy_consumption_kcal = valid_daily_energy_consumption_function(daily_energy_consumption)
# print()
#
# calculate_macronutrients_object = CalculateMacronutrients(valid_daily_energy_consumption_kcal)
# calculate_macronutrients_object.calculate_macronutrients()
# print(calculate_macronutrients_object.__repr__())
#
#
# print("""
#
#          THANK YOU FOR USING MY
#        !CALCULATE MACRONUTRIENTS!
# """)
