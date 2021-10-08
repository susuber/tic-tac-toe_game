# tic-tac-toe game

import os


def title_line():
    """Displays a line with the game title"""
    os.system('cls||clear')
    print("\n", "*" * 10, "Игра в крестики-нолики", "*" * 10, "\n\n\n")


def welcome_screen():
    """Displays the welcome screen. Registers players"""
    while True:
        title_line()

        name_player1 = input(" Первый игрок введите свое имя:\n ")
        name_player2 = input(" Второй игрок введите свое имя:\n ")

        if name_player1 == name_player2:
            title_line()
            print(" Имена играков должны отличатся\n\n ")
            os.system("pause")  # Works on Windows
            os.system('read -sn 1 -p "Press any key to continue..."')  # Works on Linux and MacOS
        else:
            break

    title_line()
    print(f" Привет {name_player1} и {name_player2} начнем игру\n\n\n  ")
    os.system("pause")
    os.system('read -sn 1 -p "Press any key to continue..."')

    return name_player1, name_player2


def print_board(board):
    """Printing the playing field"""
    title_line()

    print("", "-" * 13)
    for i in range(3):
        print(" |", board[0 + i * 3], "|", board[1 + i * 3], "|", board[2 + i * 3], "|")
        print("", "-" * 13)


def player_move(board, move):
    """ Рrocessing a player's move recorded in a string"""
    while True:
        global ability_cancel_move, number

        title_line()
        print_board(board)

        if move % 2 == 1:
            print(f"\n\n Ходит игрок {name_player1}\n"
                  f"\n")
        else:
            print(f" Ходит игрок {name_player2}\n"
                  f"\n")

        number = input(" Введите номер клетки, для вызова справки введите help: ")

        if number == "help":
            help_user()
            continue

        if number == "cancel":
            cancel_move(move, board, number, ability_cancel_move)
            continue

        try:
            number = int(number)
        except TypeError:
            print(' Число должно быть целыми от 1 до 9\n\n\n ')
            os.system("pause")
            os.system('read -sn 1 -p "Press any key to continue..."')
            continue

        if 1 > number > 9:
            title_line()
            print(' Число должно быть целыми от 1 до 9\n\n\n ')
            os.system("pause")
            os.system('read -sn 1 -p " Press any key to continue..."')
            continue

        if str(board[number - 1]) in "XO":
            print(" Данное поле занято\n\n\n")
            os.system("pause")
            os.system('read -sn 1 -p "Press any key to continue..."')
            continue

        if move % 2 == 1:
            board[number - 1] = "X"
            ability_cancel_move = True
            move += 1
            break
        else:
            board[number - 1] = "O"
            ability_cancel_move = True
            move += 1
            break

    return board, number


def check_winner(board):
    """Сhecking for a winner"""
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (1, 4, 7),
                 (0, 3, 6), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for i in win_coord:
        if board[i[0]] == board[i[1]] == board[i[2]]:
            return True
    return False


def ask():
    """Сhecking if they want to play again"""
    title_line()
    answer = input(f" Сыграем ещё?\n"
                   f" введите y или n:")
    if answer == "y":
        return True
    else:
        return False


def help_user():
    """Сalling the game help"""
    title_line()
    print(" Правила игры:\n"
          " Игроки по очереди ставят на свободные клетки поля 3х3 \n"
          " знаки (один всегда крестики, другой всегда нолики). \n"
          " Первый, выстроивший в ряд 3 своих фигуры по вертикали, \n"
          " горизонтали или диагонали, выигрывает. \n"
          " Первый ход делает игрок, ставящий крестики.\n\n"
          " Поле состоит из полей пронумерованных от 1 до 9\n\n"
          " -------------\n"
          " | 1 | 2 | 3 |\n"
          " -------------\n"
          " | 4 | 5 | 6 |\n"
          " -------------\n"
          " | 7 | 8 | 9 |\n"
          " -------------\n\n\n")
    os.system("pause")
    os.system('read -sn 1 -p "Press any key to continue..."')

    title_line()
    print(" Игроки по очереди вводят номера свободных полей\n\n"
          " Пример:\n\n"
          " Введите номер клетки, для вызова справки введите help: 1\n\n"
          " -------------\n"
          " | X | 2 | 3 |\n"
          " -------------\n"
          " | 4 | 5 | 6 |\n"
          " -------------\n"
          " | 7 | 8 | 9 |\n"
          " -------------\n\n\n")
    os.system("pause")
    os.system('read -sn 1 -p "Press any key to continue..."')

    title_line()
    print(" Для отмены хода требуется ввести cancel\n"
          " Отменить можно только один последний ход\n\n"
          " Пример:\n\n"
          " Введите номер клетки, для вызова справки введите help: cancel\n\n"
          " -------------\n"
          " | 1 | 2 | 3 |\n"
          " -------------\n"
          " | 4 | 5 | 6 |\n"
          " -------------\n"
          " | 7 | 8 | 9 |\n"
          " -------------\n\n\n")
    os.system("pause")
    os.system('read -sn 1 -p "Press any key to continue..."')


def cancel_move(move, board, number, ability_cancel_move):
    """Canceling the last move"""
    if ability_cancel_move:
        move -= 1
        board[number - 1] = str(number)
    else:
        print(" Отмена более одного хода запрещена.")


name_player1, name_player2 = welcome_screen()

while True:
    board = list(range(1, 10))
    ability_cancel_move = False
    move = 0

    while True:
        title_line()
        print_board(board)
        move += 1

        board = player_move(board, move)

        if check_winner(board):
            title_line()
            print_board(board)
            print(f" Победил {name_player1}") if move % 2 == 1 else print(f" Победил {name_player2}")
            break

        if move == 9:
            title_line()
            print_board(board)
            print(" Ничья!!!\n\n ")
            os.system("pause")
            os.system('read -sn 1 -p "Press any key to continue..."')
            break

    if ask():
        continue
    else:
        break
