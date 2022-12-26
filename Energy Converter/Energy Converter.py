import re


def valid_kcal_function(some_kcal: str):
    # if some_kcal.isdigit():
    #     return int(some_kcal)
    regex_plus_int = r"^(\d+)$"
    match = re.search(regex_plus_int, some_kcal)
    if match:
        valid_some_kcal = int(match.group(1))
        return valid_some_kcal
    regex_float_comma = r"^(\d{1,}\,{1}\d{1,})$"
    match = re.search(regex_float_comma, some_kcal)
    if match:
        current_match = match.group(1)
        current_kcal_as_string = current_match.replace(",", ".")
        valid_some_kcal = float(current_kcal_as_string)
        return valid_some_kcal
    regex_float_point = r"^(\d{1,}\.{1}\d{1,})$"
    match = re.search(regex_float_point, some_kcal)
    if match:
        current_match = match.group(1)
        valid_some_kcal = float(current_match)
        return valid_some_kcal
    else:
        raise SystemExit("Invalid kcal. Try again...")


def valid_kj_function(some_kj: str):
    # if some_kj.isdigit():
    #     return int(some_kj)
    regex_plus_int = r"^(\d+)$"
    match = re.search(regex_plus_int, some_kj)
    if match:
        valid_some_kj = int(match.group(1))
        return valid_some_kj
    regex_float_comma = r"^(\d{1,}\,{1}\d{1,})$"
    match = re.search(regex_float_comma, some_kj)
    if match:
        current_match = match.group(1)
        current_kj_as_string = current_match.replace(",", ".")
        valid_some_kj = float(current_kj_as_string)
        return valid_some_kj
    regex_float_point = r"^(\d{1,}\.{1}\d{1,})$"
    match = re.search(regex_float_point, some_kj)
    if match:
        current_match = match.group(1)
        valid_some_kj = float(current_match)
        return valid_some_kj
    else:
        raise SystemExit("Invalid kJ. Try again...")


def converter_from_kcal_to_kj_function(current_kcal):
    valid_current_kj = current_kcal * 4.18
    return valid_current_kj


def converter_from_kj_to_kcal_function(current_kj):
    valid_current_kcal = current_kj * 0.24
    return valid_current_kcal


print("""
              WELCOME TO MY
            "ENERGY CONVERTER"

""")
while True:
    options = input("""Choose converter:
    [1] - from kcal to kJ
    [2] - from kJ to kcal
    """)
    if options == "1":
        kcal = input("Enter kcal: ")
        valid_kcal = valid_kcal_function(kcal)
        kj = converter_from_kcal_to_kj_function(valid_kcal)
        print(f"{valid_kcal} kcal = {kj:.2f} kJ\n\n")
    elif options == "2":
        kj = input("Enter kJ: ")
        valid_kj = valid_kj_function(kj)
        kcal = converter_from_kj_to_kcal_function(valid_kj)
        print(f"{valid_kj} kJ = {kcal:.2f} kcal\n\n")
    else:
        raise SystemExit("Invalid choice. Try again...")
        # print("Invalid choice. Try again...")
        # break
    command = input("Click [Enter] to convert again.\n\n")
    if command == "":
        continue
    else:
        print("""             THANK YOU FOR USING MY
               ENERGY CONVERTER!
        """)
        break
