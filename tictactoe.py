import re

COORDINATES = {"1,1", "1,2", "1,3",
               "2,1", "2,2", "2,3",
               "3,1", "3,2", "3,3"}

PLAYER_SYMBOLS = {
    1: "X",
    2: "O"
}

OPPONENTS = {
    1: 2,
    2: 1
}

WIN_LOCATIONS = {
    "row1": {"1,1", "1,2", "1,3"},
    "row2": {"2,1", "2,2", "2,3"},
    "row3": {"3,1", "3,2", "3,3"},
    "column1": {"1,1", "2,1", "3,1"},
    "column2": {"1,2", "2,2", "3,2"},
    "column3": {"1,3", "2,3", "3,3"},
    "diagonal1": {"1,1", "2,2", "3,3"},
    "diagonal2": {"1,3", "2,2", "3,1"}
}


def welcome_message() -> None:
    print("Welcome to Ashley's 2-player Tic Tac Toe!"
          "\n\tGet ready to have some fun!"
          "\n\nHere is the board layout:")


def generate_board() -> dict:
    """
    Generates an empty board layout
    :return: dict: primary board setup.
    """
    return {
        "1,1": "_",
        "1,2": "_",
        "1,3": "_",
        "2,1": "_",
        "2,2": "_",
        "2,3": "_",
        "3,1": "_",
        "3,2": "_",
        "3,3": "_",
    }


def print_board(board: dict) -> None:
    print("\n\tGame Board" + "\t"*5 + "Coordinates\n"
          f"\n|\t{board['1,1']}\t{board['1,2']}\t{board['1,3']}\t|"
          "\t\t|\t(1,1)\t(1,2)\t(1,3)\t|" # end of line 1
          f"\n|\t{board['2,1']}\t{board['2,2']}\t{board['2,3']}\t|"
          "\t\t|\t(2,1)\t(2,2)\t(2,3)\t|" # end of line 2
          f"\n|\t{board['3,1']}\t{board['3,2']}\t{board['3,3']}\t|"
          "\t\t|\t(3,1)\t(3,2)\t(3,3)\t|\n" # end of line 3
          )


def player_instructions(player: int) -> str:
    print(f"Player {player}, enter coordinates '<row>,<column>' to place your '{PLAYER_SYMBOLS[player]}'" 
          "\n\tor enter 'q' to quit the game.")


def move_is_valid(player_move: str, board: dict) -> bool:
    if player_move in COORDINATES:
        if board[player_move] == '_':
            return True
    return False


def player_quits(player_move: str) -> bool:
    if re.fullmatch("[Qq]", player_move) or player_move.lower == 'quit':
        return True
    return False


def quit_message(player: int) -> None:
    print(f"Player {player} has quit the game.")


def invalid_input(input: str) -> None:
    print(f"\nI'm sorry, {input} is not valid."
          " Check that your square is free and try again.\n")


def is_winner(player_move: str, board: dict) -> bool:
    for win_locations in WIN_LOCATIONS.keys():
        winning_sequence = WIN_LOCATIONS[win_locations]
        if player_move in winning_sequence:
            player_moves_in_sequence = set()
            for square in winning_sequence:
                player_moves_in_sequence.add(board[square])
            if len(player_moves_in_sequence) == 1:
                return True
    return False


def end_of_game_message(winner: int) -> None:
    if winner:
        print(f"!!PLAYER {winner} HAS WON THE GAME!!\n"
              f"!!CONGRATULATIONS PLAYER {winner}!!")
    else:
        print("The game is a draw - an even match!")
    pass


def play() -> None:
    """
    Game algorithm for a simple 2-player CLI Tic Tac Toe game.
    :return: None
    """
    welcome_message()
    board = generate_board()
    print_board(board)
    active_player = 1
    winner = None
    turn_number = 1
    while True:
        player_instructions(active_player)
        player_move = re.sub(r"[()\s]", "", input("Coordinates: "))
        if move_is_valid(player_move, board):
            board[player_move] = PLAYER_SYMBOLS[active_player]
        elif player_quits(player_move):
            winner = OPPONENTS[active_player]
            quit_message(active_player)
            break
        else:
            invalid_input(player_move)
            continue
        print_board(board)
        if is_winner(player_move, board):
            winner = active_player
            break
        if turn_number == 9:
            break
        turn_number += 1
        active_player = OPPONENTS[active_player]

    end_of_game_message(winner)

