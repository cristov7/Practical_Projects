# class InvalidPatternChoiceError(Exception):
#     """Invalid pattern choice!"""


def choice_pattern_function():
    type_of_pattern = input("Choice type of pattern:"
                            "\n -> Triangle   [T]"
                            "\n -> Square     [S]"
                            "\n -> Rhombus    [R]"
                            "\nEnter pattern choice: ").upper()
    type_of_pattern_dict = {"T": "triangle", "TRIANGLE": "triangle",
                            "S": "square", "SQUARE": "square",
                            "R": "rhombus", "RHOMBUS": "rhombus"}
    if type_of_pattern in type_of_pattern_dict.keys():
        type_of_pattern = type_of_pattern_dict[type_of_pattern]
        try:
            size_of_pattern = int(input("Enter pattern size: "))
        except ValueError as value_error:
            print("\n\nInvalid size of pattern!"
                  "\nIt must be an integer!\n\n")
            raise SystemExit
        else:
            print("\n")
            return type_of_pattern, size_of_pattern
    else:
        # raise InvalidPatternChoiceError("Invalid pattern choice!")
        print("\n\nInvalid pattern choice!"
              "\nIt must be one of the options above!\n\n")
        raise SystemExit


def print_pattern_data_function(space, star):
    print(" " * space + "* " * star)


def get_pattern_data_function(*data):
    pattern, size = data
    if pattern == "triangle":
        # print("\n\nTriangle\n")
        for line in range(size):
            space_data = size - line - 1
            stars_data = line + 1
            print_pattern_data_function(space_data, stars_data)
    elif pattern == "square":
        # print("\n\nSquare\n")
        for line in range(size):
            space_data = 0
            stars_data = size
            print_pattern_data_function(space_data, stars_data)
    elif pattern == "rhombus":
        # print("\n\nRhombus\n")
        for line in range(size):
            space_data = size - line - 1
            stars_data = line + 1
            print_pattern_data_function(space_data, stars_data)
        for line in range(size - 2, -1, - 1):
            space_data = size - line - 1
            stars_data = line + 1
            print_pattern_data_function(space_data, stars_data)
    else:
        print("\n\nError...\n\n")


get_pattern_data_function(*choice_pattern_function())
