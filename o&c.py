
FIRST_COLUMN = ["a", "b", "c", "d", "e", ]
FIRST_ROW = ["1", "2", "3", "4", "5", ]
PLAYERS = ["Mario", "Marta", ]


def start():
    if " " in PLAYERS:
        print("ALARM! MALICIOUS CODE!")
    print("Добро пожаловать в крестики нолики!")
    print("Выберите размерность поля: 3, 4 или 5")

    size = input()
    if size not in ["3", "4", "5", ]:
        print("Неверно выбрана размерность.")
        return
    size = int(size)

    matrix = [[" "] * size for i in range(size)]

    player = PLAYERS[0]

    while check_win(matrix):
        print_field(matrix)
        player = make_turn(matrix, player)


def make_turn(matrix: list, player: str) -> str:
    """"Ввод нового хода и передача хода, если не было ошибок """
    print("Ходит игрок: " + player)
    turn = input()
    r = turn[0]
    c = turn[1]
    if r not in FIRST_COLUMN:
        print("Неверный ввод ряда")
        return player
    if c not in FIRST_ROW:
        print("Неверный ввод столбца")
        return player
    if matrix[(FIRST_COLUMN.index(r))][int(c) - 1] != " ":
        print("Позиция занята. Выберите другую")
        return player
    matrix[(FIRST_COLUMN.index(r))][int(c) - 1] = player
    return [p for p in PLAYERS if p != player][0]


def print_field(matrix: list):
    """"Функция отрисовки поля"""
    size = len(matrix)

    first_col_width = len(max(FIRST_COLUMN, key=len))
    col_width = []
    for col in range(size):
        columns = [matrix[row][col] for row in range(size)]
        columns.append(FIRST_ROW[col])
        col_width.append(len(max(columns, key=len)))

    separator = "-+-".join(["-" * first_col_width] + ["-" * n for n in col_width])

    result = [" ", ]
    for col in range(size):
        item = FIRST_ROW[col].center(col_width[col])
        result.append(item)
    print(" | ".join(result))

    for row in range(size):
        result = []
        print(separator)
        result.append(FIRST_COLUMN[row].center(first_col_width))
        for col in range(size):
            item = matrix[row][col].center(col_width[col])
            result.append(item)
        print(" | ".join(result))
    return


def check_win(matrix: list) -> bool:
    """Функция проверки условий победы"""
    size = len(matrix)
    for player in PLAYERS:
        victory_marks = []
        diagonal = [player for i in range(size) if matrix[i][i] == player]                      #В списке сохраняются все ходы на диагонали
        reverse_diagonal = [player for i in range(size) if matrix[i][size - i - 1] == player]   #В списке сохраняются все ходы на обратной диагонали
        for i in range(size):
            victory_marks.append([player for j in range(size) if matrix[j][i] == player])       #В списки сохраняются ходы в колонках
        for i in range(size):
            victory_marks.append([player for j in range(size) if matrix[i][j] == player])       #В списки сохраняются ходы в строчках
        victory_marks.append(diagonal)
        victory_marks.append(reverse_diagonal)
        for mark in victory_marks:
            if len(mark) == size:                                                               #Если в линии было сделано ходов по размерности матрицы, то игрок выиграл
                print("".join(["Игрок ", player, " выиграл!", ]))
                print_field(matrix)
                return False
    return True


if __name__ == '__main__':
    start()
