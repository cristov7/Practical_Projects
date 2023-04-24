# class InvalidPatternChoiceError(Exception):
#     """Invalid pattern choice!"""


# class InvalidPatternSizeError(Exception):
#     """Invalid pattern size!"""


def choice_pattern_function():
    type_of_pattern_dict = {"T": "triangle", "TRIANGLE": "triangle",
                            "S": "square", "SQUARE": "square",
                            "R": "rhombus", "RHOMBUS": "rhombus"}

    type_of_pattern = input("Choice type of pattern:"
                            "\n -> Triangle   [T]"
                            "\n -> Square     [S]"
                            "\n -> Rhombus    [R]"
                            "\nEnter pattern choice: ").upper()

    if type_of_pattern in type_of_pattern_dict.keys():
        type_of_pattern = type_of_pattern_dict[type_of_pattern]

        try:
            size_of_pattern = int(input("Enter pattern size: "))

        except ValueError:
            raise SystemExit("\n\nInvalid size of pattern!"
                             "\nIt must be an integer!")
            # raise InvalidPatternSizeError("Invalid pattern size!")

        else:
            print("\n")
            return type_of_pattern, size_of_pattern

    else:
        raise SystemExit("\n\nInvalid pattern choice!"
                         "\nIt must be one of the options above!")
        # raise InvalidPatternChoiceError("Invalid pattern choice!")


def print_pattern_data_function(space, star):
    print(" " * space + "* " * star)


def get_pattern_data_function(*data):
    pattern, size = data

    if pattern == "triangle":
        for line in range(size):
            space_data = size - line - 1
            stars_data = line + 1
            print_pattern_data_function(space_data, stars_data)

    elif pattern == "square":
        for line in range(size):
            space_data = 0
            stars_data = size
            print_pattern_data_function(space_data, stars_data)

    elif pattern == "rhombus":

        for line in range(size):
            space_data = size - line - 1
            stars_data = line + 1
            print_pattern_data_function(space_data, stars_data)

        for line in range(size - 2, -1, - 1):
            space_data = size - line - 1
            stars_data = line + 1
            print_pattern_data_function(space_data, stars_data)


get_pattern_data_function(*choice_pattern_function())
