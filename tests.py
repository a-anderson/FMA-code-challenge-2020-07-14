import pytest
import tictactoe

def test_always_passes() -> None:
    assert True, "This should pass"


def test_always_fails() -> None:
    assert False, "This should fail"


def test_move_is_valid_coordinates_pass() -> None:
    assert tictactoe.move_is_valid("1,3") == True, "Accepts good co-ordinate input"


def test_move_is_valid_q_pass() -> None:
    assert tictactoe.move_is_valid("q") == True and tictactoe.move_is_valid("Q") == True, "Accepts quit"


def test_move_is_valid_fail() -> None:
    assert tictactoe.move_is_valid("1,4") == False, "Rejects invalid player input"

# TODO: Test the final play function.