import random
import pytest

from classes.player import EasyComputerPlayer
from main import place_ships, play

random.seed(42)


@pytest.mark.timeout(5)
def test_full_random_gameplay():
    player_1, player_2 = EasyComputerPlayer("Player 1"), EasyComputerPlayer("Player 2")

    place_ships(player_1)
    place_ships(player_2)

    winner = play(player_1, player_2, horizontal=True)

    assert winner is player_2
