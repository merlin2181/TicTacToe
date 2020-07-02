# write your code
'''
A text based game of Tic Tac Toe.  The user enters a string containing X, O or _
The computer tells you if you won, which character won, if you draw, if the game isn't finished
or if there was an impossible case.
'''


def check_diagonal(moves):
    ''' checks if there is a winning game in the diagonals'''
    dia_check = []
    if moves[0][0] == moves[1][1] == moves[2][2]:
        dia_check.append(moves[1][1])
    if moves[0][2] == moves[1][1] == moves[2][0]:
        dia_check.append(moves[1][1])
    return dia_check


def check_columns(moves):
    ''' checks if there is a winning game in the columns'''
    col_check = []
    if moves[0][0] == moves[1][0] == moves[2][0]:
        col_check.append(moves[0][0])
    if moves[0][1] == moves[1][1] == moves[2][1]:
        col_check.append(moves[0][1])
    if moves[0][2] == moves[1][2] == moves[2][2]:
        col_check.append(moves[0][2])
    return col_check


def check_rows(moves):
    ''' checks if there is a winning game in the rows '''
    row_check = []
    if moves[0][0] == moves[0][1] == moves[0][2]:
        row_check.append(moves[0][0])
    if moves[1][0] == moves[1][1] == moves[1][2]:
        row_check.append(moves[1][0])
    if moves[2][0] == moves[2][1] == moves[2][2]:
        row_check.append(moves[2][0])
    return row_check


def check_x_o(moves):
    ''' returns a true / false flag if there are more X's (O's) than O's (X's) '''
    x_list = [char for group in moves for char in group if char == "X"]
    o_list = [char for group in moves for char in group if char == "O"]
    difference = abs(len(x_list) - len(o_list))
    if difference >= 2:
        print("Impossible")
        return True
    return False


def impossible_case(diagonal, column, rows):
    ''' returns a true / false flag to see if an impossible situation occurred '''
    if len(diagonal) >= 2:
        return True
    if len(column) >= 2:
        return True
    if len(rows) >= 2:
        return True
    if len(diagonal) == 1 and len(column) == 1:
        return True
    if len(diagonal) == 1 and len(rows) == 1:
        return True
    if len(column) == 1 and len(rows) == 1:
        return True
    return False


def draw_case(diagonal, column, rows, char_count):
    ''' returns a true / false flag to see if the game is a draw'''
    if len(diagonal) == 0 and len(column) == 0 and len(rows) == 0 and len(char_count) == 9:
        return True
    return False


def change_coordinates(coor):
    ''' convert user input coordinates to matrix coordinates '''
    y = int(coor[0]) - 1
    x = int(coor[1]) - 1
    return x, y


def check_coordinates(coor):
    numbers = [['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'],
               ['0', '4', '5', '6', '7', '8', '9']]
    for i in range(len(coor)):
        if coordinates[i] in numbers[0] and coordinates[i] in numbers[1]:
            print("Coordinates should be from 1 to 3!")
            return True
        elif coordinates[i] not in numbers[0]:
            print("You should enter numbers!")
            return True
    return False


def draw_gameboard(game_list):
    ''' print out user input in a tic tac toe board '''
    print("---------")
    print("|", game_list[2][0], game_list[2][1], game_list[2][2], "|")
    print("|", game_list[1][0], game_list[1][1], game_list[1][2], "|")
    print("|", game_list[0][0], game_list[0][1], game_list[0][2], "|")
    print("---------")


user_input = input("Enter cells: ")  # get user input
cells = [user_input[i] for i in range(len(user_input))]  # turn user_input into a list of moves
cells = [" " if cells[i] == "_" else cells[i] for i in range(len(cells))]  # convert "_" to an empty space

# create a matrix with the user input
matrix = [[cell for cell in cells[-3:]], [cell for cell in cells[-6:-3]],
          [cell for cell in cells[-9:-6]]]

draw_gameboard(matrix)

while True:
    flag = True
    while flag:
        coordinates = input("Enter the coordinates: ").split()
        flag = check_coordinates(coordinates)
    i, j = change_coordinates(coordinates)
    if matrix[i][j] == " ":
        matrix[i][j] = "X"
        break
    else:
        print("This cell is occupied! Choose another one!")
        continue

draw_gameboard(matrix)

'''
# code to see what the outcome of the game is
if not check_x_o(matrix):
    diag = check_diagonal(matrix)
    col = check_columns(matrix)
    row = check_rows(matrix)
    if impossible_case(diag, col, row):
        print("Impossible")
    else:
        # count all the X's and O's in the game
        count = [char for words in matrix for char in words if char == "X" or char == "O"]
        # count all the empty spaces in the game
        count_empty = [char for words in matrix for char in words if char == " "]
        # determine outcome
        if draw_case(diag, col, row, count):
            print("Draw")
        elif len(diag) == 0 and len(col) == 0 and len(row) == 0 and len(count_empty) > 0:
            print("Game not finished")
        elif len(diag) == 1
            print(f"{diag[0][1]} wins")
        elif len(col) == 1:
            print(f"{col[0][1]} wins")
        elif len(row) == 1:
            print(f"{row[0][1]} wins")
'''
