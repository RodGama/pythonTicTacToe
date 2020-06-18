counter = 0
count_x = 0
count_o = 0
matrix = []
player = "X"
x = 1
for i in range(0, 3, 1):
    matrix.append([])
    for j in range(0, 3, 1):
        matrix[i].append("_")
row_1_win = False
row_2_win = False
row_3_win = False
dia_1_win = False
dia_2_win = False
col_1_win = False
col_2_win = False
col_3_win = False
print("---------")
print("| " + matrix[0][0] + " " + matrix[0][1] + " " + matrix[0][2] + " | ")
print("| " + matrix[1][0] + " " + matrix[1][1] + " " + matrix[1][2] + " | ")
print("| " + matrix[2][0] + " " + matrix[2][1] + " " + matrix[2][2] + " | ")
print("---------")
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
while x == 1:
    if count_o + count_x == 9:
        print("Draw")
        break
    jogada_2 = str(input("Enter the coordinates: > ")).split()
    while jogada_2[0] not in numbers or jogada_2[1] not in numbers:
        print("You should enter numbers!")
        jogada_2 = str(input("Enter the coordinates: > ")).split()

    while int(jogada_2[0]) > 3 or int(jogada_2[1]) > 3:
        print("Coordinates should be from 1 to 3!")
        jogada_2 = str(input("Enter the coordinates: > ")).split()

    while int(jogada_2[0]) < 1 or int(jogada_2[1]) < 1:
        print("Coordinates should be from 1 to 3!")
        jogada_2 = str(input("Enter the coordinates: > ")).split()

    while matrix[3 - int(jogada_2[1])][int(jogada_2[0]) - 1] == "X" or matrix[3 - int(jogada_2[1])][int(jogada_2[0]) - 1] == "O":
        print(matrix[3 - int(jogada_2[1])][int(jogada_2[0]) - 1])
        print("This cell is occupied! Choose another one!")
        jogada_2 = str(input("Enter the coordinates: > ")).split()

    matrix[3 - int(jogada_2[1])][int(jogada_2[0]) - 1] = player
    if player == "X":
        count_x = count_x + 1
        player = "O"
    else:
        count_o = count_o + 1
        player = "X"
    print("---------")
    print("| " + matrix[0][0] + " " + matrix[0][1] + " " + matrix[0][2] + " | ")
    print("| " + matrix[1][0] + " " + matrix[1][1] + " " + matrix[1][2] + " | ")
    print("| " + matrix[2][0] + " " + matrix[2][1] + " " + matrix[2][2] + " | ")
    print("---------")

    if matrix[0][0] == matrix[0][1] == matrix[0][2] and matrix[0][0] != "_":
        row_1_win = True  # primeira linha
        print(matrix[0][0] + " wins")
        break
    if matrix[1][0] == matrix[1][1] == matrix[1][2] and matrix[1][0] != "_":
        row_2_win = True  # segunda linha
        print(matrix[1][0] + " wins")
        break
    if matrix[2][0] == matrix[2][1] == matrix[2][2] and matrix[2][0] != "_":
        row_3_win = True  # terceira linha
        print(matrix[2][0] + " wins")
        break
    if matrix[0][0] == matrix[1][1] == matrix[2][2] and matrix[0][0] != "_":
        dia_1_win = True  # diagonal  0 9
        print(matrix[0][0] + " wins")
        break
    if matrix[0][2] == matrix[1][1] == matrix[2][0] and matrix[0][2] != "_":
        dia_2_win = True  # diagonal 3 7
        print(matrix[0][2] + " wins")
        break
    if matrix[0][0] == matrix[1][0] == matrix[2][0] and matrix[0][0] != "_":
        col_1_win = True  # primeira coluna
        print(matrix[0][0] + " wins")
        break
    if matrix[0][1] == matrix[1][1] == matrix[2][1] and matrix[0][1] != "_":
        col_2_win = True  # segunda coluna
        print(matrix[0][1] + " wins")
        break
    if matrix[0][2] == matrix[1][2] == matrix[2][2] and matrix[0][2] != "_":
        col_3_win = True  # terceira coluna
        print(matrix[0][2] + " wins")
        break
