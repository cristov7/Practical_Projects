import re


def valid_gender_function(current_gender: str):
    current_gender = current_gender.lower()
    genders_dict = {"f": "woman", "female": "woman", "m": "man", "male": "man"}
    if current_gender in genders_dict:
        valid_current_gender = genders_dict[current_gender]
        return valid_current_gender
    else:
        raise SystemExit("Invalid gender. Try again...")


def valid_kg_function(current_kg: str):
    # if current_kg.isdigit():
    #     return int(current_kg)
    regex_plus_int = r"^(\d+)$"
    match = re.search(regex_plus_int, current_kg)
    if match:
        valid_current_kg = int(match.group(1))
        return valid_current_kg
    regex_plus_float_point = r"^(\d{1,}\.{1}\d{1,})$"
    match = re.search(regex_plus_float_point, current_kg)
    if match:
        valid_current_kg = float(match.group(1))
        return valid_current_kg
    regex_plus_float_comma = r"^(\d{1,}\,{1}\d{1,})$"
    match = re.search(regex_plus_float_comma, current_kg)
    if match:
        current_match = match.group(1)
        current_kg_as_string = current_match.replace(",", ".")
        valid_current_kg = float(current_kg_as_string)
        return valid_current_kg
    else:
        raise SystemExit("Invalid weigh. Try again in kg...")


def valid_cm_function(current_cm: str):
    # if current_kg.isdigit():
    #     return int(current_kg)
    regex_plus_int = r"^(\d+)$"
    match = re.search(regex_plus_int, current_cm)
    if match:
        valid_current_cm = int(match.group(1))
        return valid_current_cm
    regex_plus_float_point = r"^(\d{1,}\.{1}\d{1,})$"
    match = re.search(regex_plus_float_point, current_cm)
    if match:
        valid_current_cm = float(match.group(1))
        return valid_current_cm
    regex_plus_float_comma = r"^(\d{1,}\,{1}\d{1,})$"
    match = re.search(regex_plus_float_comma, current_cm)
    if match:
        current_match = match.group(1)
        current_cm_as_string = current_match.replace(",", ".")
        valid_current_cm = float(current_cm_as_string)
        return valid_current_cm
    else:
        raise SystemExit("Invalid height. Try again in cm...")


def valid_age_function(current_age: str):
    # if current_age.isdigit():
    #     return int(current_age)
    regex_plus_int = r"^(\d+)$"
    match = re.search(regex_plus_int, current_age)
    if match:
        valid_current_age = int(match.group(1))
        return valid_current_age
    else:
        raise SystemExit("Invalid age. Try again...")


def main_exchange_function(some_gender: str, some_kg, some_cm, some_age: int):
    if some_gender == "woman":
        current_main_exchange = (10 * some_kg) + (6.25 * some_cm) - (4.9 * some_age) - 161
        return current_main_exchange
    # elif some_gender == "man":
    else:
        current_main_exchange = (10 * some_kg) + (6.25 * some_cm) - (4.9 * some_age) + 5
        return current_main_exchange


def valid_physical_activity_factor_function(current_physical_activity_factor):
    current_physical_activity_factor = current_physical_activity_factor.lower()
    physical_activity_factor_dict = {"1": 1.2, "sedentary way of life": 1.2,
                                     "2": 1.375, "light physical activity": 1.375,
                                     "3": 1.55, "moderate physical activity": 1.55,
                                     "4": 1.725, "high physical activity": 1.725,
                                     "5": 1.9, "very high physical activity": 1.9}
    if current_physical_activity_factor in physical_activity_factor_dict:
        valid_current_physical_activity_factor = physical_activity_factor_dict[current_physical_activity_factor]
        return valid_current_physical_activity_factor
    else:
        raise SystemExit("Invalid factor. Try again...")


def daily_energy_consumption_factor_function(some_main_exchange: float, some_physical_activity_factor: float):
    current_daily_energy_consumption = some_main_exchange * some_physical_activity_factor
    return current_daily_energy_consumption


print("""
             DETERMINATION OF
        "DAILY ENERGY CONSUMPTION"

""")
while True:
    gender = input("""Genders:
    [M] - Male
    [F] - Female
    Enter your gender: """)
    valid_gender = valid_gender_function(gender)
    kg = input("Enter your weigh in kg: ")
    valid_kg = valid_kg_function(kg)
    cm = input("Enter your height in cm: ")
    valid_cm = valid_cm_function(cm)
    age = input("Enter your age: ")
    valid_age = valid_age_function(age)
    main_exchange = main_exchange_function(valid_gender, valid_kg, valid_cm, valid_age)
    print(f"\n\nYour Main Exchange is {main_exchange:.2f} kcal.\n\n")
    physical_activity_factor = input("""Level of physical activity:
    [1] - Sedentary way of life
    [2] - Light physical activity
    [3] - Moderate physical activity
    [4] - High physical activity
    [5] - Very high physical activity
    Enter your level: """)
    valid_physical_activity_factor = valid_physical_activity_factor_function(physical_activity_factor)
    daily_energy_consumption = daily_energy_consumption_factor_function(main_exchange, valid_physical_activity_factor)
    print(f"\n\nDaily Energy Consumption: {daily_energy_consumption:.2f} kcal.\n\n")
    command = input("Click [Enter] to calculating again.")
    if command == "":
        continue
    else:
        print("""
                     
          THANK YOU FOR USING MY
        "DAILY ENERGY CONSUMPTION"
        """)
        break
