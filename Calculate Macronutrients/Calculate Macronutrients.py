import re


def valid_daily_energy_consumption_function(some_kcal: str):
    # if some_kcal.isdigit():
    #     return int(some_kcal)
    regex_int = r"^(\d+)$"
    match = re.search(regex_int, some_kcal)
    if match:
        valid_kcal = int(match.group(1))
        return valid_kcal
    regex_float_point = r"^(\d{1,}\.{1}\d{1,})$"
    match = re.search(regex_float_point, some_kcal)
    if match:
        valid_kcal = float(match.group(1))
        return valid_kcal
    regex_float_comma = r"^(\d{1,}\,{1}\d{1,})$"
    match = re.search(regex_float_comma, some_kcal)
    if match:
        current_match = match.group(1)
        current_kcal_as_string = current_match.replace(",", ".")
        valid_kcal = float(current_kcal_as_string)
        return valid_kcal
    else:
        raise SystemExit("Invalid kcal. Try again...")


def calculate_macronutrients_function(some_daily_energy_consumption_kcal):
    macronutrients_percent_dict = {"Protein": 15,
                                   "Fat": 30,
                                   "Carb": 55}
    current_protein_kcal = some_daily_energy_consumption_kcal * (macronutrients_percent_dict["Protein"] / 100)
    current_fat_kcal = some_daily_energy_consumption_kcal * (macronutrients_percent_dict["Fat"] / 100)
    current_carb_kcal = some_daily_energy_consumption_kcal * (macronutrients_percent_dict["Carb"] / 100)
    current_macronutrients_kcal_dict = {"Protein": current_protein_kcal,
                                        "Fat": current_fat_kcal,
                                        "Carb": current_carb_kcal}
    return current_macronutrients_kcal_dict


print("""
              Healthy Eating
         Calculate Macronutrients
           "Protein, Fat, Carb"

""")
while True:
    daily_energy_consumption = input("Enter your kcal (target for 1 day): ")
    valid_daily_energy_consumption_kcal = valid_daily_energy_consumption_function(daily_energy_consumption)
    macronutrients_dict = calculate_macronutrients_function(valid_daily_energy_consumption_kcal)
    print("\nProtein 15 %, Fat 30 %, Carb 55 %:")
    for macronutrient, kcal in macronutrients_dict.items():
        print(f"- {macronutrient}: {kcal:.2f} kcal")
    print("\n(1 g Protein = 4,1 kcal)\n(1 g Fat = 9,3 kcal)\n(1 g Carb = 4,1 kcal)\n\n")
    command = input("Click [Enter] to convert again.")
    if command == "":
        continue
    else:
        print("""             

              THANK YOU FOR USING MY
             CALCULATE MACRONUTRIENTS!
        """)
        break
