import pytest
import tictactoe

def test_always_passes() -> None:
    assert True, "This should pass"


def test_always_fails() -> None:
    assert False, "This should fail"


def test_move_is_valid_true() -> None:
    assert tictactoe.move_is_valid("1,3") == True, "Accepts valid player input"


def test_move_is_valid_fail() -> None:
    assert tictactoe.move_is_valid("1,4") == False, "Rejects invalid player input"


def test_player_quits_true() -> None:
    assert tictactoe.player_quits("q") == True and \
           tictactoe.player_quits("Q") == True, "Accepts quit"


def test_player_quits_false() -> None:
    assert tictactoe.player_quits("no") == False and \
           tictactoe.player_quits("1,2") == False, "Rejects anything but [Qq] input"


def test_coordinate_is_free_true() -> None:
    board = tictactoe.generate_board()
    assert tictactoe.coordinate_is_free("1,1", board) == True, \
        "Correctly identifies free space on game board"


def test_coordinate_is_free_false() -> None:
    board = tictactoe.generate_board()
    test_move = "1,3"
    board[test_move] = "X"
    assert tictactoe.coordinate_is_free(test_move, board) == False, \
        "Correctly identifies occupied space on board"

# TODO: Test the final play function.