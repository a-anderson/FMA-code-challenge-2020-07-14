import re
import time

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

DIVIDER = f"{'=' * 40}"

def welcome_message() -> None:
    print("Welcome to Ashley's 2-player Tic Tac Toe!"
          "\n\tGet ready to have some fun!")


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
    print("Here is the current board layout:\n"
          "\n\tGame Board" + "\t"*4 + "Coordinates\n"
          f"\n|\t{board['1,1']}\t{board['1,2']}\t{board['1,3']}\t|"
          "\t|\t(1,1)\t(1,2)\t(1,3)\t|" # end of line 1
          f"\n|\t{board['2,1']}\t{board['2,2']}\t{board['2,3']}\t|"
          "\t|\t(2,1)\t(2,2)\t(2,3)\t|" # end of line 2
          f"\n|\t{board['3,1']}\t{board['3,2']}\t{board['3,3']}\t|"
          "\t|\t(3,1)\t(3,2)\t(3,3)\t|\n" # end of line 3
          )


def player_instructions(player: int) -> None:
    print(f"Player {player}, enter coordinates '<row>,<column>' to place your '{PLAYER_SYMBOLS[player]}'" 
          "\n\tor enter 'q' to quit the game.")


def print_divider(time_delay=False) -> None:
    if time_delay:
        for char in DIVIDER:
            print(char, end="", flush=True)
            time.sleep(0.015)
        print("\n")
    else:
        print(DIVIDER)


def move_is_valid(player_move: str, board: dict) -> bool:
    if player_move in COORDINATES:
        if board[player_move] == '_':
            return True
    return False


def print_valid_move(player: int) -> None:
    print(f"\nGood move player {player}!")


def player_quits(player_move: str) -> bool:
    if re.fullmatch("[Qq]", player_move) or player_move.lower() == 'quit':
        return True
    return False


def quit_message(player: int) -> None:
    print(f"Player {player} has quit the game.")
    time.sleep(1)


def invalid_input(input: str) -> None:
    print(f"\nI'm sorry, {input} is not valid."
          " Check that your square is free and try again.\n")
    print_divider(time_delay=True)


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
        print("GAME OVER")


def play() -> None:
    """
    Game algorithm for a simple 2-player CLI Tic Tac Toe game.
    :return: None
    """
    welcome_message()
    print_divider()
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
            print_valid_move(active_player)
        elif player_quits(player_move):
            quit_message(active_player)
            break
        else:
            invalid_input(player_move)
            print_board(board)
            continue
        print_divider(time_delay=True)
        print_board(board)
        if is_winner(player_move, board):
            winner = active_player
            break
        if turn_number == 9:
            break
        turn_number += 1
        active_player = OPPONENTS[active_player]

    print_divider()
    end_of_game_message(winner)
    print_divider()

if __name__ == "__main__":
    while True:
        play()
        play_again = input("Would you like to play again? [Y/n]").strip().lower()
        if not play_again == 'y' and play_again:
            break
    print("Thank you for playing Ashley's Tic Tac Toe.\n\tI hope you had fun!")
