# Game Structure
# player = 'X'/1
# winner = None
# display instructions
#
# while True:
#     player instruction message
#     console input
#         --> check for [Qq] --> quit game --> display victory by default message
#         --> check valid coordinate
#         --> check coordinate not taken
#     convert to actionable data format
#     place entry onto board
#     display board
#     check win condition --> winner = player --> break
#         --> row victory
#         --> column victory
#         --> diagonal victory
#     check if the board is full --> if full --> break
#     switch players
#
# print game results to console

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

def welcome_message() -> None:
    print("Welcome to Ashley's 2-player Tic Tac Toe!"
          "\n\tGet ready to have some fun!"
          "\n\nHere is the board layout:")

def generate_board() -> dict:
    """
    Generates an empty board layout
    :return: dict: primary board setup.
    """
    board = {
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
    return board


def print_board(board: dict) -> None:
    print("\n\tYour Board" + "\t"*5 + "Coordinates\n"
          f"\n|\t{board['1,1']}\t{board['1,2']}\t{board['1,3']}\t|"
          "\t\t|\t(1,1)\t(1,2)\t(1,3)\t|" # end of line 1
          f"\n|\t{board['2,1']}\t{board['2,2']}\t{board['2,3']}\t|"
          "\t\t|\t(2,1)\t(2,2)\t(2,3)\t|" # end of line 2
          f"\n|\t{board['3,1']}\t{board['3,2']}\t{board['3,3']}\t|"
          "\t\t|\t(3,1)\t(3,2)\t(3,3)\t|\n" # end of line 3
          )

def player_instructions(player: int) -> str:
    print(f"Player {player}, enter coordinates row,column to place your {PLAYER_SYMBOLS[player]}" 
          "\n\tor enter q to quit the game.")


def play() -> None:
    '''
    Game algorithm for a simple 2-player CLI Tic Tac Toe game.
    :return: None
    '''
    welcome_message()
    board = generate_board()
    print_board(board)
    active_player = 1
    winner = None
    while True:
        player_instructions(active_player)
        break

    pass
