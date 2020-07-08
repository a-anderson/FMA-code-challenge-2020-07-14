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
    assert tictactoe.player_quits("q") == True and tictactoe.player_quits("Q") == True, "Accepts quit"


def test_player_quits_false() -> None:
    assert tictactoe.player_quits("no") == False and tictactoe.player_quits("1,2") == False, "Rejects anything but [Qq] input"




# TODO: Test the final play function.