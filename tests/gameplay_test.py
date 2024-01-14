import random
import pytest
import pickle
from unittest.mock import patch

from classes.game import Game
from classes.player import BeginnerComputerPlayer, SmartComputerPlayer
from errors.input_exceptions import UnknownGameObjectException
from main import begin_game, resume_game, place_ships

random.seed(42)


@pytest.mark.timeout(5)
def test_full_random_gameplay():
    game = Game(BeginnerComputerPlayer("Player 1"),
                BeginnerComputerPlayer("Player 2"))

    begin_game(game)

    assert game.winner is game.player_1


@pytest.mark.timeout(10)
def test_full_stategy_gameplay():
    game = Game(SmartComputerPlayer("Player 1"),
                BeginnerComputerPlayer("Player 2"))

    begin_game(game)

    assert game.winner is game.player_1


@pytest.mark.timeout(10)
def test_game_replayability():
    TOTAL_GAMES = 5
    game = Game(BeginnerComputerPlayer("Player 1"),
                BeginnerComputerPlayer("Player 2"))

    begin_game(game, number_sets=TOTAL_GAMES)

    assert game.total_games_played == TOTAL_GAMES
    assert game.finished

@pytest.mark.parametrize("game_object", [
    pickle.dumps("Not a game object"),
    b'Also not a game object',
    ])
def test_paused_game_object_error(game_object):
    with pytest.raises(UnknownGameObjectException):
        Game.resume_game_set(game_object)


@pytest.mark.timeout(5)
def test_finished_paused_game_flow():
    game = Game(BeginnerComputerPlayer("Player 1"),
                BeginnerComputerPlayer("Player 2"))

    begin_game(game, number_sets=1)

    assert game.finished

    game = Game.resume_game_set(game.pause_game_set())

    assert game.finished
    assert game.paused
    assert game.total_games_played == 1


@pytest.mark.timeout(5)
def test_unfinished_paused_game_flow():
    game = Game(BeginnerComputerPlayer("Player 1"),
                BeginnerComputerPlayer("Player 2"))

    begin_game(game, number_sets=1, horizontal=True)

    assert game.finished
    assert game.total_games_played == 1

    game.reset_game_set()

    place_ships(game.player_1)
    place_ships(game.player_2)

    initial_player = game.next_turn()

    assert not game.finished

    paused_game = game.pause_game_set()

    game = Game.resume_game_set(paused_game)

    assert not game.finished
    assert game.paused
    # Finished game and the game ongoing
    assert game.total_games_played == 2

    # Assert the next player is the same as the initial player
    starting_player = game.next_turn()
    assert initial_player.name == starting_player.name

    game.next_turn()

    with patch('main.place_ships', side_effect=Exception('boats are trying to be placed again, but they should not be')):
        begin_game(game, number_sets=1, horizontal=True)

    assert game.finished
    assert not game.paused
    assert game.total_games_played == 2

