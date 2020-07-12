import pytest
import tictactoe


def generate_filled_board(win_state, player_move, winning_locations) -> dict:
    board = tictactoe.generate_board()
    if win_state:
        for location in winning_locations:
            board[location] = 'X'
    else:
        for location in winning_locations:
            if location == player_move:
                board[location] = 'X'
            else:
                board[location] = '0'
    return board


@pytest.mark.parametrize("input_coordinate, expected_output, output_str",
                         [("1,3", True, "Accepts valid player input"),
                          ("1,4", False, "Rejects invalid player input"),
                          ("1,1", False, "Rejects if square already taken")])
def test_move_is_valid(input_coordinate, expected_output, output_str) -> None:
    board = tictactoe.generate_board()
    occupied_square = "1,1"
    board[occupied_square] = 'X'
    assert tictactoe.move_is_valid(input_coordinate, board) == expected_output, \
        output_str


@pytest.mark.parametrize("player_input, expected_output",
                         [("q", True), ("Q", True), ("no", False), ("1,2", False)])
def test_player_quits(player_input, expected_output) -> None:
    assert tictactoe.player_quits(player_input) == expected_output, \
        "Correctly accepts/rejects quit input"


@pytest.mark.parametrize("expected_outcome, output_str",
                         [(True, "Returns True for winning move"),
                          (False, "Returns False for non-winning move")])
def test_is_winner(expected_outcome, output_str) -> None:
    for winning_locations in tictactoe.WIN_LOCATIONS.keys():
        winning_squares = tictactoe.WIN_LOCATIONS[winning_locations]
        player_move = min(winning_squares)
        board = generate_filled_board(expected_outcome, player_move, winning_squares)
        assert tictactoe.is_winner(player_move, board) is expected_outcome, \
            output_str


@pytest.mark.parametrize("winner, expected_output, output_str",
                         [(None, "GAME OVER\n", "Prints no winner message if draw"),
                          (2, ("!!PLAYER 2 HAS WON THE GAME!!\n"
                               "!!CONGRATULATIONS PLAYER 2!!\n"),
                           "Prints winning message if winner")])
def test_end_of_game_message(capsys, winner, expected_output, output_str) -> None:
    tictactoe.end_of_game_message(winner)
    out, err = capsys.readouterr()
    assert out == expected_output, output_str


@pytest.mark.parametrize("input_coordinates, expected_output",
                         [(["1,1", "2,2", "2,1", "1,3", "3,1"],
                           "!!CONGRATULATIONS PLAYER 1!!\n"),
                          (["1,1", "2,2", "2,1", "1,3", "1,2", "3,1"],
                           "!!CONGRATULATIONS PLAYER 2!!\n"),
                          (["2,2", "1,2", "1,3", "1,1", "2,1", "2,3", "3,2", "3,1", "3,3"],
                           "GAME OVER\n")
                          ])
def test_play(capsys, input_coordinates, expected_output) -> None:

    def mock_input(s):
        return input_coordinates.pop(0)

    tictactoe.input = mock_input
    tictactoe.play()
    out, err = capsys.readouterr()
    str_length = len(expected_output) + len(tictactoe.DIVIDER) + 1
    assert out[-str_length:] == f"{expected_output}{tictactoe.DIVIDER}\n", \
        "Play correctly prints winning player"
