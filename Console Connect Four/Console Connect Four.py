def create_matrix_list_function():
    min_possible_length = 4
    count_nested_lists = 0
    count_nested_elements = 0
    while True:
        count_rows = int(input("Enter number of rows: "))
        if count_rows < min_possible_length:
            print(f"\n\nIt must be more that {count_rows} rows!\n"
                  f"Please, try again more or equal than {min_possible_length}!\n\n")
        else:
            count_nested_lists = count_rows
            break
    while True:
        count_columns = int(input("Enter number of columns: "))
        if count_columns < min_possible_length:
            print(f"\n\nIt must be more that {count_columns} columns!\n"
                  f"Please, try again more or equal than {min_possible_length}!\n\n")
            print(f"Enter number of rows: {count_nested_lists}")
        else:
            count_nested_elements = count_columns
            break
    create_matrix_list = []
    for index_nested_list in range(count_nested_lists):
        nested_list = []
        for index_nested_elements in range(count_nested_elements):
            nested_element = 0
            nested_list.append(nested_element)
        create_matrix_list.append(nested_list)
    return create_matrix_list


def return_number_of_players_function(max_possible_players):
    min_players = 2
    while True:
        number_of_players = int(input("\nEnter number of players: "))
        if number_of_players < min_players:
            print(f"\n\nIt must be more players!"
                  f"\nPlease, try again between {min_players} and {max_possible_players} players!\n")
        elif number_of_players > max_possible_players:
            print(f"\n\nThere are too many players!"
                  f"\nPlease, try again between {min_players} and {max_possible_players} players!\n")
        else:
            return number_of_players


def return_player_choice_column_function(player_number: int, max_possible_columns: int):
    while True:
        player_choice_column = int(input(f"\n\nPlayer {player_number}, please choose a column: "))
        if player_choice_column > max_possible_columns:
            print(f"\n\nInvalid column! Please enter valid column!")
        else:
            index_nested_element = player_choice_column - 1
            return index_nested_element


def return_matrix_list_after_action(current_matrix_list, player_index_nested_element, number):

    def check_horizontal_function():
        for index_nested_list in range(len(current_matrix_list) - 1, -1, - 1):
            for index_nested_element in range(len(current_matrix_list[index_nested_list]) - 3):
                first_nested_element = current_matrix_list[index_nested_list][index_nested_element]
                second_nested_element = current_matrix_list[index_nested_list][index_nested_element + 1]
                third_nested_element = current_matrix_list[index_nested_list][index_nested_element + 2]
                fourth_nested_element = current_matrix_list[index_nested_list][index_nested_element + 3]
                if first_nested_element == second_nested_element == third_nested_element == fourth_nested_element\
                        == number:
                    return "Match!"
                else:
                    continue
        return "No match!"

    def check_vertical_function():
        for index_nested_element in range(len(current_matrix_list[0])):
            for index_nested_list in range(len(current_matrix_list) - 3):
                first_nested_element = current_matrix_list[index_nested_list][index_nested_element]
                second_nested_element = current_matrix_list[index_nested_list + 1][index_nested_element]
                third_nested_element = current_matrix_list[index_nested_list + 2][index_nested_element]
                fourth_nested_element = current_matrix_list[index_nested_list + 3][index_nested_element]
                if first_nested_element == second_nested_element == third_nested_element == fourth_nested_element\
                        == number:
                    return "Match!"
                else:
                    continue
        return "No match!"

    def check_first_diagonal_function():
        for index_nested_list in range(len(current_matrix_list) - 3):
            for index_nested_element in range(len(current_matrix_list[index_nested_list]) - 3):
                first_nested_element = current_matrix_list[index_nested_list][index_nested_element]
                second_nested_element = current_matrix_list[index_nested_list + 1][index_nested_element + 1]
                third_nested_element = current_matrix_list[index_nested_list + 2][index_nested_element + 2]
                fourth_nested_element = current_matrix_list[index_nested_list + 3][index_nested_element + 3]
                if first_nested_element == second_nested_element == third_nested_element == fourth_nested_element\
                        == number:
                    return "Match!"
                else:
                    continue
        return "No match!"

    def check_second_diagonal_function():
        for index_nested_list in range(len(current_matrix_list) - 1, 3, - 1):
            for index_nested_element in range(len(current_matrix_list[index_nested_list]) - 3):
                first_nested_element = current_matrix_list[index_nested_list][index_nested_element]
                second_nested_element = current_matrix_list[index_nested_list - 1][index_nested_element + 1]
                third_nested_element = current_matrix_list[index_nested_list - 2][index_nested_element + 2]
                fourth_nested_element = current_matrix_list[index_nested_list - 3][index_nested_element + 3]
                if first_nested_element == second_nested_element == third_nested_element == fourth_nested_element\
                        == number:
                    return "Match!"
                else:
                    continue
        return "No match!"

    def check_free_space_function():
        coordinates_list = []
        for index_nested_element in range(len(current_matrix_list[0])):
            for index_nested_list in range(len(current_matrix_list) - 1, -1, - 1):
                nested_element = current_matrix_list[index_nested_list][index_nested_element]
                if nested_element == 0:
                    coordinates_list = [index_nested_list, index_nested_element]
                    return coordinates_list
                else:
                    continue
        return coordinates_list

    while True:
        for nested_list_index in range(len(current_matrix_list) - 1, -1, - 1):
            if current_matrix_list[nested_list_index][player_index_nested_element] == 0:
                current_matrix_list[nested_list_index][player_index_nested_element] = number
                print()
                print(*current_matrix_list, sep="\n")
                check_horizontal = check_horizontal_function()
                check_vertical = check_vertical_function()
                check_first_diagonal = check_first_diagonal_function()
                check_second_diagonal = check_second_diagonal_function()
                if "Match!" in [check_horizontal, check_vertical, check_first_diagonal, check_second_diagonal]:
                    print(f"\n\n         The winner is player {number}!\n\n")
                    raise SystemExit
                else:
                    free_space_list = check_free_space_function()
                    if free_space_list:
                        return current_matrix_list
                    else:
                        print("\n\n         There is no space left!\n\n               GAME OVER\n\n")
                        raise SystemExit
            else:
                continue
        player_index_nested_element += 1
        print(f"\nThere is no space in the column number {player_index_nested_element}!")
        if player_index_nested_element == len(current_matrix_list[0]):
            print("\nSearching for a free space...")
            free_space_list = check_free_space_function()
            if free_space_list:
                nested_list_index, nested_element_index = free_space_list
                current_matrix_list[nested_list_index][nested_element_index] = number
                print()
                print(*current_matrix_list, sep="\n")
                check_horizontal = check_horizontal_function()
                check_vertical = check_vertical_function()
                check_first_diagonal = check_first_diagonal_function()
                check_second_diagonal = check_second_diagonal_function()
                if "Match!" in [check_horizontal, check_vertical, check_first_diagonal, check_second_diagonal]:
                    print(f"\n\n         The winner is player {number}!\n\n")
                    raise SystemExit
                else:
                    free_space_list = check_free_space_function()
                    if free_space_list:
                        return current_matrix_list
                    else:
                        print("\n\n         There is no space left!\n\n               GAME OVER\n\n")
                        raise SystemExit
            else:
                print("\n\n         There is no space left!\n\n               GAME OVER\n\n")
                raise SystemExit
        else:
            continue


print("""

            Welcome to my:   
         Console Connect Four
                 !!!          

""")
matrix_list = create_matrix_list_function()
max_players = len(matrix_list[0])
count_players = return_number_of_players_function(max_players)
max_columns = max_players
print("""

         Let's get started:
""")
print(*matrix_list, sep="\n")
while True:
    for number_of_player in range(1, count_players + 1):
        player_choose_index_nested_element = return_player_choice_column_function(number_of_player, max_columns)
        matrix_list = return_matrix_list_after_action(matrix_list, player_choose_index_nested_element, number_of_player)
