def sudoku_solver(board_list):

    def is_valid(number, row, column):
        # Check row and column for duplicates
        for index in range(9):
            if board_list[row][index] == number or board_list[index][column] == number:
                return False

        # Check 3x3 square for duplicates
        box_row = (row // 3) * 3
        box_col = (column // 3) * 3

        for index_nested_list in range(box_row, box_row + 3):
            for index_nested_element in range(box_col, box_col + 3):
                if board_list[index_nested_list][index_nested_element] == number:
                    return False

        # If no duplicates found, number is valid
        return True

    def get_empty_cell():
        for index_nested_list in range(9):
            for index_nested_element in range(9):
                if board_list[index_nested_list][index_nested_element] == 0:
                    return index_nested_list, index_nested_element

        return None

    def backtrack():
        empty_cell = get_empty_cell()

        if empty_cell is None:
            return True

        else:
            index_nested_list, index_nested_element = empty_cell

            for number in range(1, 10):
                if is_valid(number, index_nested_list, index_nested_element):
                    board_list[index_nested_list][index_nested_element] = number

                    if backtrack():
                        return True

                    else:
                        board_list[index_nested_list][index_nested_element] = 0

            else:
                return False

    def output():
        output_list = []
        separator_line = "-" * 25
        separation_index_list = [0, 4, 8, 12]

        for index in separation_index_list:
            board_list.insert(index, separator_line)

        for index_nested_list, row in enumerate(board_list):
            if index_nested_list in separation_index_list:
                output_list.append(row)

            else:
                row = f"| {row[0]} {row[1]} {row[2]} | {row[3]} {row[4]} {row[5]} | {row[6]} {row[7]} {row[8]} |"
                output_list.append(row)

        return "\n".join(output_list)

    if backtrack():
        output = output()
        return output

    else:
        raise SystemExit("Invalid input! Please, check for duplicates!")


board = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0]]

print(sudoku_solver(board))
