# write your code
'''
A text based game of Tic Tac Toe.  The user enters a string containing X, O or _
The computer tells you if you won, which character won, if you draw, if the game isn't finished
or if there was an impossible case.
'''


def check_diagonal(moves):
    ''' checks if there is a winning game in the diagonals'''
    dia = ""
    dia_check = []
    exes = ["X", "X", "X"]
    oohs = ["O", "O", "O"]
    for i in range(3):
        if moves[i][i] == "X" or moves[i][i] == "O":
            dia_check.append(moves[i][i])
        else:
            dia_check.append(" ")
    if dia_check == exes or dia_check == oohs:
        dia = dia_check[0]
        return dia
    else:
        for i in range(3):
            j = 2
            check_dia = []
            for i in range(3):
                check_dia.append(moves[i][j])
                j -= 1
            if check_dia == exes or check_dia == oohs:
                dia = check_dia[0]
        return dia


def check_columns(moves):
    ''' checks if there is a winning game in the columns'''
    col = ""
    check = [[], [], []]
    exes = ["X", "X", "X"]
    oohs = ["O", "O", "O"]
    for i in range(len(moves)):
        for j in range(len(moves)):
            if moves[j][i] == "X" or moves[j][i] == "O":
                check[j].append(moves[j][i])
            else:
                check[j].append(" ")
    for i in range(len(check)):
        if check[i] == exes or check[i] == oohs:
            col = check[i][0]
            return col
    return col


def check_rows(moves):
    ''' checks if there is a winning game in the rows '''
    rows = ""
    check = [[], [], []]
    exes = ["X", "X", "X"]
    oohs = ["O", "O", "O"]
    for i in range(len(moves)):
        for j in range(len(moves)):
            if moves[i][j] == "X" or moves[i][j] == "O":
                check[i].append(moves[i][j])
            else:
                check[i].append(" ")
    for i in range(len(check)):
        if check[i] == exes or check[i] == oohs:
            rows = check[i][0]
            return rows
    return rows


def check_x_o(moves):
    ''' returns a true / false flag if there are more X's (O's) than O's (X's) '''
    x_list = [char for group in moves for char in group if char == "X"]
    o_list = [char for group in moves for char in group if char == "O"]
    difference = abs(len(x_list) - len(o_list))
    if difference >= 2:
        print("Impossible")
        return True
    return False


def draw_case(diagonal, column, rows):
    ''' returns a true / false flag to see if the game is a draw'''
    count = [char for words in matrix for char in words if char == "X" or char == "O"]
    if len(diagonal) == 0 and len(column) == 0 and len(rows) == 0 and len(count) == 9:
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


matrix = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
draw_gameboard(matrix)
move = 0
while True:
    flag = True
    while flag:
        coordinates = input("Enter the coordinates: ").split()
        flag = check_coordinates(coordinates)
    i, j = change_coordinates(coordinates)
    if matrix[i][j] == " ":
        if move % 2 == 0:
            matrix[i][j] = "X"
            move += 1
        else:
            matrix[i][j] = "O"
            move += 1
        draw_gameboard(matrix)
        diag = check_diagonal(matrix)
        col = check_columns(matrix)
        row = check_rows(matrix)
        if draw_case(diag, col, row):
            print("Draw")
            break
        elif len(diag) == 1:
            print(f"{diag} wins")
            break
        elif len(col) == 1:
            print(f"{col} wins")
            break
        elif len(row) == 1:
            print(f"{row} wins")
            break
        else:
            continue
    else:
        print("This cell is occupied! Choose another one!")
        continue


