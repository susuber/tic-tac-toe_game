# tic-tac-toe game

import os


def title_line():
    """Displays a line with the game title"""
    # clearing the screen and print the game title
    os.system('cls||clear')  # clearing the screen
    print("\033[32m\n", "*" * 10, "Игра в крестики-нолики", "*" * 10, "\n\n\n\033[37m")


def welcome_screen():
    """Displays the welcome screen. Registers players"""
    while True:
        # clearing the screen and print the game title
        title_line()

        # entering player names
        name_player1 = input(" Первый игрок введите свое имя:\n ")
        name_player2 = input(" Второй игрок введите свое имя:\n ")

        if name_player1 == name_player2:
            title_line()
            print(" Имена играков должны отличатся\n\n ")
            # Stopping the system
            os.system("pause")  # Works on Windows
            os.system('read -sn 1 -p "Для продолжения нажмите любую клавишу..."')  # Works on Linux and MacOS
        else:
            break

    # clearing the screen and print the game title
    title_line()
    # welcome players
    print(f" Привет {name_player1} и {name_player2} начнем игру\n\n\n  ")
    # Stopping the system
    os.system("pause")  # Works on Windows
    os.system('read -sn 1 -p "Для продолжения нажмите любую клавишу..."')  # Works on Linux and MacOS

    return name_player1, name_player2


def print_board(board):
    """Printing the playing field"""
    # clearing the screen and print the game title
    title_line()

    # Printing the playing field
    print("", "-" * 13)
    for i in range(3):
        print(" |", board[0 + i * 3], "|", board[1 + i * 3], "|", board[2 + i * 3], "|")
        print("", "-" * 13)


def player_move(board, move):
    """ Рrocessing a player's move recorded in a string"""
    while True:
        global ability_cancel_move, number_old

        # clearing the screen and print the game title
        title_line()
        # print the game board
        print_board(board)

        # choosing a walking player
        if move % 2 == 1:
            print(f"\033[31m\n\n Ходит игрок {name_player1}\n"
                  f"\n\033[37m")
        else:
            print(f"\033[31m\n\n Ходит игрок {name_player2}\n"
                  f"\n\033[37m")

        number = input(" Введите номер клетки, для вызова справки введите help: ")

        if number == "help":
            help_user()
            continue

        if number == "cancel":
            ability_cancel_move, move = cancel_move(board, ability_cancel_move, number_old)
            continue

        # checking that an integer is entered
        if not number.isdigit():
            title_line()
            print('\033[31m Введите целое число от 1 до 9\n\n\n \033[37m')
            os.system("pause")
            os.system('read -sn 1 -p "Для продолжения нажмите любую клавишу..."')
            continue
        elif number.find(".") != -1:
            title_line()
            print('\033[31m Введите целое число от 1 до 9\n\n\n \033[37m')
            os.system("pause")
            os.system('read -sn 1 -p "Для продолжения нажмите любую клавишу..."')
            continue

        # checking possible unaccounted errors
        try:
            number = int(number)
        except ValueError:
            title_line()
            print('\033[31m Введите целое число от 1 до 9\n\n\n \033[37m')
            os.system("pause")
            os.system('read -sn 1 -p "Для продолжения нажмите любую клавишу..."')
            continue

        # checking that the number falls within the board limits
        if (1 > number) or (number > 9):
            title_line()
            print('\033[31m Число должно быть целыми от 1 до 9\n\n\n \033[37m')
            os.system("pause")
            os.system('read -sn 1 -p " Для продолжения нажмите любую клавишу..."')
            continue

        # checking that the field is not occupied
        if str(board[number - 1]) in "XO":
            print("\n\n\033[31m Данное поле занято\n\033[37m")
            os.system("pause")
            os.system('read -sn 1 -p "Для продолжения нажмите любую клавишу..."')
            continue

        # remember the number for the possibility of canceling the move
        number_old = number

        # put a cross or a zero in the selected field
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

    return board


def check_winner(board):
    """Сhecking for a winner"""
    # creating a tuple of possible winning options
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (1, 4, 7),
                 (0, 3, 6), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    # check if there is no winner
    for i in win_coord:
        if board[i[2]] == board[i[0]] == board[i[1]]:
            return True
    return False


def ask():
    """Сhecking if they want to play again"""
    title_line()
    answer = input(f" Сыграем ещё?\n"
                   f" введите y или yes для повторной игры: ")
    if answer == "y" or answer == "yes":
        return True
    else:
        return False


def help_user():
    """Сalling the game help"""
    # clearing the screen and print the game title
    title_line()
    print(" \033[31mПравила игры:\n\033[37m"
          " Игроки по очереди ставят на свободные клетки поля 3х3 \n"
          " знаки (один всегда крестики, другой всегда нолики). \n"
          " Первый, выстроивший в ряд 3 своих фигуры по вертикали, \n"
          " горизонтали или диагонали, выигрывает. \n"
          " Первый ход делает игрок, ставящий крестики.\n\n"
          " \033[31mПоле состоит из полей пронумерованных от 1 до 9\n\n\033[37m"
          " -------------\n"
          " | 1 | 2 | 3 |\n"
          " -------------\n"
          " | 4 | 5 | 6 |\n"
          " -------------\n"
          " | 7 | 8 | 9 |\n"
          " -------------\n\n\n")
    # Stopping the system
    os.system("pause")  # Works on Windows
    os.system('read -sn 1 -p "Для продолжения нажмите любую клавишу..."')  # Works on Linux and MacOS

    # clearing the screen and print the game title
    title_line()
    print(" Игроки по очереди вводят номера свободных полей\n\n"
          " \033[31mПример:\n\n\033[37m"
          " Введите номер клетки, для вызова справки введите help: 1\n\n"
          " -------------\n"
          " |\033[31m X \033[37m| 2 | 3 |\n"
          " -------------\n"
          " | 4 | 5 | 6 |\n"
          " -------------\n"
          " | 7 | 8 | 9 |\n"
          " -------------\n\n\n")
    # Stopping the system
    os.system("pause")  # Works on Windows
    os.system('read -sn 1 -p "Для продолжения нажмите любую клавишу..."')  # Works on Linux and MacOS

    # clearing the screen and print the game title
    title_line()
    print(" Для отмены хода требуется ввести cancel\n"
          " Отменить можно только один последний ход\n\n"
          "\033[31m Пример:\n\n\033[37m"
          " Введите номер клетки, для вызова справки введите help: cancel\n\n"
          " -------------\n"
          " |\033[31m 1 \033[37m| 2 | 3 |\n"
          " -------------\n"
          " | 4 | 5 | 6 |\n"
          " -------------\n"
          " | 7 | 8 | 9 |\n"
          " -------------\n\n\n")
    # Stopping the system
    os.system("pause")  # Works on Windows
    os.system('read -sn 1 -p "Для продолжения нажмите любую клавишу..."')  # Works on Linux and MacOS


def cancel_move(board, ability_cancel_move, number_old):
    """Canceling the last move"""
    global move

    if ability_cancel_move:
        move -= 1
        board[number_old - 1] = str(number_old)
        ability_cancel_move = False
        return ability_cancel_move, move
    else:
        title_line()
        print("\033[31m Отмена более одного хода запрещена.\n\n\n\033[37m")
        os.system("pause")
        os.system('read -sn 1 -p " Для продолжения нажмите любую клавишу..."')


name_player1, name_player2 = welcome_screen()

while True:
    # generate a clean playing field and reset the moves
    board = list(range(1, 10))
    ability_cancel_move = False
    move = 0

    while True:
        move += 1
        board = player_move(board, move)

        if check_winner(board):  # checking for a winner
            title_line()
            print_board(board)
            print(f"\033[31m\n\n Победил {name_player1}\n\n\033[37m") \
                if move % 2 == 1 else print(f"\033[31m\n\n Победил {name_player2}\n\n\033[37m")
            os.system("pause")
            os.system('read -sn 1 -p "Для продолжения нажмите любую клавишу..."')
            break

        if move == 9:
            title_line()
            print_board(board)
            print("\033[31m\n\n Ничья!!!\n\n \033[37m")
            os.system("pause")
            os.system('read -sn 1 -p "Для продолжения нажмите любую клавишу..."')
            break

    if ask():
        continue
    else:
        break
