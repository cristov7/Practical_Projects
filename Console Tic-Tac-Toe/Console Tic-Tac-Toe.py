def return_players_names_function():   # Who will play?
    player_names_list = []
    while True:
        if len(player_names_list) == 0:   # We don't have names!
            name = input("Player one name: ")
            player_names_list.append(name)
        elif len(player_names_list) == 1:   # We have 1 name!
            name = input("Player two name: ")
            if name not in player_names_list:   # We have another name!
                player_names_list.append(name)
            else:   # We already have that name!
                print("\n\nThe name is taken!"
                      "\nPlease, try another name!\n\n")
                print(f"Player one name: {player_names_list[0]}")
        else:   # elif len(player_names_list) == 2:   # We have 2 names!
            break
    return player_names_list


def return_order_in_the_game_function(first_player: str, second_player: str):   # Players and their symbols!
    players_chars_dict = {}
    while True:
        first_player_char = input(f"\n\n{first_player} choose operator between 'X' and 'O'!"
                                  f"\nEnter [x] or [o]: ")
        if first_player_char.upper() == "X":   # First player will play with 'X' and the second with 'O'!
            players_chars_dict[first_player] = first_player_char.upper()
            players_chars_dict[second_player] = "O"
            break
        elif first_player_char.upper() == "O":   # First player will play with 'O' and the second with 'X'!
            players_chars_dict[first_player] = first_player_char.upper()
            players_chars_dict[second_player] = "X"
            break
        else:   # Invalid symbol!
            print("\n\nInvalid symbol! Please, try again!")
    return players_chars_dict


def return_the_numeration_of_the_board_function():   # The board:
    bord_matrix_list = [["|", " ", "1", " ", "|", " ", "2", " ", "|", " ", "3", " ", "|"],
                        ["|", " ", "4", " ", "|", " ", "5", " ", "|", " ", "6", " ", "|"],
                        ["|", " ", "7", " ", "|", " ", "8", " ", "|", " ", "9", " ", "|"]]
    print("This is the numeration of the board:")
    for nested_list in bord_matrix_list:
        print(*nested_list)
    return bord_matrix_list


def return_free_positions_dict_function(matrix_list: list):   # The positions with their coordinates!
    positions_dict = {}
    for index_nested_list in range(len(matrix_list)):
        for index_nested_element in range(len(matrix_list[index_nested_list])):
            nested_element = matrix_list[index_nested_list][index_nested_element]
            if nested_element.isdigit():   # We found a position!
                positions_dict[nested_element] = [index_nested_list, index_nested_element]
            else:
                continue
    return positions_dict


def return_after_action_function(player_name: str, player_char: str):   # The main func - play!
    def return_free_position_function():   # Check the positions!
        if position in free_positions_dict.keys():
            coordinates_list = free_positions_dict[position]
            coordinate_list = coordinates_list[0]
            coordinate_element = coordinates_list[1]
            starting_board_list[coordinate_list][coordinate_element] = player_char
            del free_positions_dict[position]
            if len(free_positions_dict) > 0:
                return "True with Free Positions"   # Game on!
            else:
                return "True without Free Positions"   # That was the last turn!
        else:
            return "\n\nThat number is not free!" \
                   "\nPlease, try again!\n"   # The number was taken!

    def return_winner_function():   # Do we have a winner?
        if (starting_board_list[0][2] == player_char and starting_board_list[0][6] == player_char and starting_board_list[0][10] == player_char) or\
            (starting_board_list[1][2] == player_char and starting_board_list[1][6] == player_char and starting_board_list[1][10] == player_char) or\
            (starting_board_list[2][2] == player_char and starting_board_list[2][6] == player_char and starting_board_list[2][10] == player_char) or\
            (starting_board_list[0][2] == player_char and starting_board_list[1][2] == player_char and starting_board_list[2][2] == player_char) or\
            (starting_board_list[0][6] == player_char and starting_board_list[1][6] == player_char and starting_board_list[2][6] == player_char) or\
            (starting_board_list[0][10] == player_char and starting_board_list[1][10] == player_char and starting_board_list[2][10] == player_char) or\
            (starting_board_list[0][2] == player_char and starting_board_list[1][6] == player_char and starting_board_list[2][10] == player_char) or\
                (starting_board_list[2][2] == player_char and starting_board_list[1][6] == player_char and starting_board_list[0][10] == player_char):
            return "True"   # We have a winner!
        else:
            return "False"   # We don't have a winner!

    position_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]   # Possible positions!
    position = input(f"\n{player_name} choose a free position [1 - 9]: ")
    if position in position_list:   # Valid position!
        check_for_position = return_free_position_function()   # Check the positions!
        if check_for_position == "True with Free Positions":   # Game on!
            for nested_list in starting_board_list:
                for index, nested_element in enumerate(nested_list):
                    if nested_element.isdigit():
                        nested_list[index] = " "
                    else:
                        continue
                print(*nested_list)
            check_for_win = return_winner_function()   # Do we have a winner?
            if check_for_win == "True":   # We have a winner!
                print(f"\n\n            {player_name} won!\n\n")
                raise SystemExit
            else:   # elif check_for_win == "False":   # We don't have a winner!
                return "True"   # Game on!
        elif check_for_position == "True without Free Positions":   # That was the last turn!
            for nested_list in starting_board_list:
                for index, nested_element in enumerate(nested_list):
                    if nested_element.isdigit():
                        nested_list[index] = " "
                    else:
                        continue
                print(*nested_list)
            check_for_win = return_winner_function()   # Do we have a winner?
            if check_for_win == "True":   # We have a winner!
                print(f"\n\n            {player_name} won!\n\n")
                raise SystemExit
            else:  # elif check_for_win == "False":   # Game over!
                print("\n\n          There is no free space!"""
                      "\n\n                  Draw!\n\n")
                raise SystemExit
        else:   # elif check_for_position == "\n\nThat number is not free!\nPlease, try again!\n":
            return check_for_position   # The number was taken!
    else:   # Invalid position!
        invalid_position = "\n\nInvalid position!" \
                           "\nPlease, try again!\n"
        return invalid_position


print("""

            Console Tic-Tac-Toe:

""")
names_list = return_players_names_function()
player_1_name = names_list[0]
player_2_name = names_list[1]
chars_dict = return_order_in_the_game_function(player_1_name, player_2_name)
player_1_char = chars_dict[player_1_name]
player_2_char = chars_dict[player_2_name]
print(f"\n\n{player_1_name} will play with '{player_1_char}'!")
print(f"{player_2_name} will play with '{player_2_char}'!\n\n")
starting_board_list = return_the_numeration_of_the_board_function()
free_positions_dict = return_free_positions_dict_function(starting_board_list)
print(f"\n\n{player_1_name} starts first!\n")
while True:   # Play the game!
    player_1_turn = return_after_action_function(player_1_name, player_1_char)
    if player_1_turn == "True":   # Next player turn!
        print()
    elif player_1_turn == "\n\nThat number is not free!" \
                          "\nPlease, try again!\n":   # The number was taken!
        print(player_1_turn)
        continue
    else:   # elif player_1_turn == "\n\nInvalid position!\nPlease, try again!\n":   # Invalid position!
        print(player_1_turn)
        continue
    while True:
        player_2_turn = return_after_action_function(player_2_name, player_2_char)
        if player_2_turn == "True":   # Next player turn!
            print()
            break
        elif player_2_turn == "\n\nThat number is not free!" \
                              "\nPlease, try again!\n":   # The number was taken!
            print(player_2_turn)
            continue
        else:  # elif player_2_turn == "\n\nInvalid position!\nPlease, try again!\n":   # Invalid position!
            print(player_2_turn)
            continue
