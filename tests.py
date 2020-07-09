import pytest
import tictactoe

def test_move_is_valid_true() -> None:
    assert tictactoe.move_is_valid("1,3", tictactoe.generate_board()) == True, "Accepts valid player input"


def test_move_is_valid_fail() -> None:
    assert tictactoe.move_is_valid("1,4", tictactoe.generate_board()) == False, "Rejects invalid player input"

def test_move_is_valid_square_taken() -> None:
    board = tictactoe.generate_board()
    player_move = "1,3"
    board[player_move] = "X"
    assert tictactoe.move_is_valid(player_move, board) == False, "Rejects input if square not free"

def test_player_quits_true() -> None:
    assert tictactoe.player_quits("q") == True and \
           tictactoe.player_quits("Q") == True, "Accepts quit"


def test_player_quits_false() -> None:
    assert tictactoe.player_quits("no") == False and \
           tictactoe.player_quits("1,2") == False, "Rejects anything but [Qq] input"


def test_is_winner_return_true_if_winning_sequence() -> None:
    board = tictactoe.generate_board()
    for location in tictactoe.WIN_LOCATIONS["row1"]:
        board[location] = "X"
    assert tictactoe.is_winner("1,3", board) == True, "Returns True for winning move"


def test_is_winner_return_false_if_not_winning_sequence() -> None:
    board = tictactoe.generate_board()
    board["1,1"] = "X"
    board["1,2"] = "O"
    board["1,3"] = "x"
    assert tictactoe.is_winner("1,3", board) == False, "Returns False for non-winning move"

# TODO: Test the final play function.