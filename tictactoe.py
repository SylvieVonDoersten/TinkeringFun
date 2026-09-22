# Simple Tic-Tac-Toe game for beginners

board = [" ", " ", " ",
         " ", " ", " ",
         " ", " ", " "]


def print_board():
    print()
    print("  1 | 2 | 3")
    print("  " + board[0] + " | " + board[1] + " | " + board[2])
    print(" ---+---+---")
    print("  " + board[3] + " | " + board[4] + " | " + board[5])
    print(" ---+---+---")
    print("  " + board[6] + " | " + board[7] + " | " + board[8])
    print()


def check_winner(player):
    winning_lines = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]

    for line in winning_lines:
        if board[line[0]] == player and board[line[1]] == player and board[line[2]] == player:
            return True
    return False


def is_board_full():
    return " " not in board


def make_move(position, player):
    if position < 1 or position > 9:
        return False

    index = position - 1
    if board[index] != " ":
        return False

    board[index] = player
    return True


def play_game():
    current_player = "X"

    while True:
        print_board()
        print(f"Player {current_player}, choose a number from 1 to 9.")

        try:
            choice = int(input("Your move: "))
        except ValueError:
            print("Please enter a number.")
            continue

        if not make_move(choice, current_player):
            print("That spot is already taken or invalid. Try again.")
            continue

        if check_winner(current_player):
            print_board()
            print(f"Player {current_player} wins! 🎉")
            break

        if is_board_full():
            print_board()
            print("It's a draw! 🤝")
            break

        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"


print("Welcome to Tic-Tac-Toe!")
play_game()
print("Thanks for playing!")
