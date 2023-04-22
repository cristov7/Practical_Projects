# import re


class DailyEnergyConsumption:
    def __init__(self, weight: float, height: float, age: int, gender: str, physical_activity_factor: float):
        self.weight = weight
        self.height = height
        self.age = age
        self.gender = gender
        self.physical_activity_factor = physical_activity_factor
        self.main_exchange: None or float = None
        self.daily_energy_consumption: None or float = None

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

    @property   # getter
    def age(self) -> int:
        return self.__age

    @age.setter   # setter
    def age(self, value: int) -> [None, ValueError]:
        if isinstance(value, int) and 0 < value <= 100:
            self.__age = value
        else:
            raise ValueError("Invalid age. Try again...")

    def calculate_main_exchange(self) -> None:
        if self.main_exchange is None:

            if self.gender == "man":
                self.main_exchange = (10 * self.weight) + (6.25 * self.height) - (4.9 * self.age) + 5

            elif self.gender == "woman":
                self.main_exchange = (10 * self.weight) + (6.25 * self.height) - (4.9 * self.age) - 161

    def calculate_daily_energy_consumption(self) -> None:
        if self.main_exchange is None:

            self.calculate_main_exchange()
            self.calculate_daily_energy_consumption()

        else:
            self.daily_energy_consumption = self.main_exchange * self.physical_activity_factor

    def __repr__(self) -> str:
        if self.main_exchange and self.daily_energy_consumption:
            output_list = ["Calculation:"]

            main_exchange_info = f"- Main Exchange: {self.main_exchange:.2f} kcal."
            daily_energy_consumption_info = f"- Daily Energy Consumption: {self.daily_energy_consumption:.2f} kcal."
            output_list.extend([main_exchange_info, daily_energy_consumption_info])

            output = "\n".join(output_list)
            return output
        else:
            return "First you have to calculate main exchange and daily energy consumption!"


# print("""
#              DETERMINATION OF
#         "DAILY ENERGY CONSUMPTION"
#
# """)
#
#
# def valid_weight_and_height_function(value: str):
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
#         raise SystemExit("Invalid value. Try again in kg...")
#
#
# def valid_age_function(value: str):
#     regex_plus_int = r"^(\d+)$"
#     match = re.search(regex_plus_int, value)
#     if match:
#         valid_value = int(match.group(1))
#         return valid_value
#     else:
#         raise SystemExit("Invalid value. Try again...")
#
#
# def valid_gender_function(value: str):
#     genders_dict = {"m": "man", "male": "man",
#                     "f": "woman", "female": "woman"}
#     if value.lower() in genders_dict.keys():
#         valid_value = genders_dict[value.lower()]
#         return valid_value
#     else:
#         raise SystemExit("Invalid value. Try again...")
#
#
# def valid_physical_activity_factor_function(value: str):
#     physical_activity_factor_dict = {"1": 1.2, "sedentary way of life": 1.2,
#                                      "2": 1.375, "light physical activity": 1.375,
#                                      "3": 1.55, "moderate physical activity": 1.55,
#                                      "4": 1.725, "high physical activity": 1.725,
#                                      "5": 1.9, "very high physical activity": 1.9}
#     if value.lower() in physical_activity_factor_dict.keys():
#         valid_value = physical_activity_factor_dict[value.lower()]
#         return valid_value
#     else:
#         raise SystemExit("Invalid value. Try again...")
#
#
# current_kg = input("Enter your weigh in kg: ")
# valid_kg = valid_weight_and_height_function(current_kg)
#
# current_cm = input("Enter your height in cm: ")
# valid_cm = valid_weight_and_height_function(current_cm)
#
# current_age = input("Enter your age: ")
# valid_age = valid_age_function(current_age)
#
# current_gender = input("""\n\nGender options:
# [M] - Male
# [F] - Female
#
# Enter your gender: """)
# valid_gender = valid_gender_function(current_gender)
#
# current_physical_activity_factor = input("""\n\nLevel of physical activity:
# [1] - Sedentary way of life
# [2] - Light physical activity
# [3] - Moderate physical activity
# [4] - High physical activity
# [5] - Very high physical activity
#
# Enter your level: """)
# valid_physical_activity_factor = valid_physical_activity_factor_function(current_physical_activity_factor)
#
#
# daily_energy_consumption_object = DailyEnergyConsumption(valid_kg, valid_cm, valid_age, valid_gender, valid_physical_activity_factor)
# daily_energy_consumption_object.calculate_main_exchange()
# daily_energy_consumption_object.calculate_daily_energy_consumption()
# print("\n")
# print(daily_energy_consumption_object.__repr__())
#
#
# print("""
#
#           THANK YOU FOR USING MY
#         "DAILY ENERGY CONSUMPTION"
# """)
