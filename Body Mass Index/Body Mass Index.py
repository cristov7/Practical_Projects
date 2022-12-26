import re


def valid_kg_function(some_kg: str):
    # if some_kg.isdigit():
    #     return int(some_kg)
    regex_int = r"^(\d+)$"
    match = re.search(regex_int, some_kg)
    if match:
        valid_some_kg = int(match.group(1))
        return valid_some_kg
    regex_float_point = r"^(\d{1,}\.{1}\d{1,})$"
    match = re.search(regex_float_point, some_kg)
    if match:
        valid_some_kg = float(match.group(1))
        return valid_some_kg
    regex_float_comma = r"^(\d{1,}\,{1}\d{1,})$"
    match = re.search(regex_float_comma, some_kg)
    if match:
        current_match = match.group(1)
        some_kg_as_string = current_match.replace(",", ".")
        valid_some_kg = float(some_kg_as_string)
        return valid_some_kg
    else:
        raise SystemExit("Invalid weigh. Try again in kg...")


def valid_cm_function(some_meters: str):
    # if some_meters.isdigit():
    #     return int(some_meters)
    regex_int = r"^(\d+)$"
    match = re.search(regex_int, some_meters)
    if match:
        valid_some_meters = int(match.group(1))
        return valid_some_meters
    regex_float_point = r"^(\d{1,}\.{1}\d{1,})$"
    match = re.search(regex_float_point, some_meters)
    if match:
        valid_some_meters = float(match.group(1))
        return valid_some_meters
    regex_float_comma = r"^(\d{1,}\,{1}\d{1,})$"
    match = re.search(regex_float_comma, some_meters)
    if match:
        current_match = match.group(1)
        some_meters_as_string = current_match.replace(",", ".")
        valid_some_meters = float(some_meters_as_string)
        return valid_some_meters
    else:
        raise SystemExit("Invalid height. Try again in meters...")


def body_mass_index_function(current_kg, current_meters):
    current_body_mass_index = current_kg / current_meters ** 2
    if current_body_mass_index <= 24.9:
        return "0th degree of obesity"
    elif current_body_mass_index <= 29.9:
        return "1st degree of obesity"
    elif current_body_mass_index <= 39.9:
        return "2nd degree of obesity"
    else:
        return "3rd degree of obesity"


print("""
              Welcome to my
            "Body Mass Index"
            
""")
while True:
    kg = input("Enter your weigh in kg: ")
    valid_kg = valid_kg_function(kg)
    meters = input("Enter your height in meters: ")
    valid_meters = valid_cm_function(meters)
    body_mass_index = body_mass_index_function(valid_kg, valid_meters)
    print(f"\nBody Mass Index:\n{body_mass_index}.\n\n")
    command = input("Click [Enter] to calculating again.")
    if command == "":
        continue
    else:
        print("""
    
          THANK YOU FOR USING MY
            "BODY MASS INDEX!"
        """)
        break
