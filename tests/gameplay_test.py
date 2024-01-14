import random
import pytest

from classes.game import Game
from classes.player import BeginnerComputerPlayer, SmartComputerPlayer
from main import begin_game

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
