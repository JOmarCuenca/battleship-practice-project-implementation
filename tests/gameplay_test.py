import random
import pytest

from classes.player import BeginnerComputerPlayer, SmartComputerPlayer
from main import place_ships, play

random.seed(42)


@pytest.mark.timeout(5)
def test_full_random_gameplay():
    player_1, player_2 = BeginnerComputerPlayer("Player 1"), BeginnerComputerPlayer("Player 2")

    place_ships(player_1)
    place_ships(player_2)

    winner = play(player_1, player_2)

    assert winner is player_1

@pytest.mark.timeout(10)
def test_full_stategy_gameplay():
    player_1, player_2 = SmartComputerPlayer("Player 1"), BeginnerComputerPlayer("Player 2")

    place_ships(player_1)
    place_ships(player_2)

    winner = play(player_1, player_2)

    assert winner is player_1
