from classes.ship import *
from constants.directions import Direction

import pytest


@pytest.mark.parametrize("ship, direction, expected", [
    (Carrier, Direction.UP, [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)]),
    (Battleship, Direction.UP, [(0, 0), (0, 1), (0, 2), (0, 3)]),
    (Cruiser, Direction.UP, [(0, 0), (0, 1), (0, 2)]),
    (Submarine, Direction.UP, [(0, 0), (0, 1), (0, 2)]),
    (Destroyer, Direction.UP, [(0, 0), (0, 1)]),
    (Carrier, Direction.DOWN, [(0, 0), (0, -1), (0, -2), (0, -3), (0, -4)]),
    (Battleship, Direction.DOWN, [(0, 0), (0, -1), (0, -2), (0, -3)]),
    (Cruiser, Direction.DOWN, [(0, 0), (0, -1), (0, -2)]),
    (Submarine, Direction.DOWN, [(0, 0), (0, -1), (0, -2)]),
    (Destroyer, Direction.DOWN, [(0, 0), (0, -1)]),
    (Carrier, Direction.LEFT, [(0, 0), (-1, 0), (-2, 0), (-3, 0), (-4, 0)]),
    (Battleship, Direction.LEFT, [(0, 0), (-1, 0), (-2, 0), (-3, 0)]),
    (Cruiser, Direction.LEFT, [(0, 0), (-1, 0), (-2, 0)]),
    (Submarine, Direction.LEFT, [(0, 0), (-1, 0), (-2, 0)]),
    (Destroyer, Direction.LEFT, [(0, 0), (-1, 0)]),
    (Carrier, Direction.RIGHT, [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0)]),
    (Battleship, Direction.RIGHT, [(0, 0), (1, 0), (2, 0), (3, 0)]),
    (Cruiser, Direction.RIGHT, [(0, 0), (1, 0), (2, 0)]),
    (Submarine, Direction.RIGHT, [(0, 0), (1, 0), (2, 0)]),
    (Destroyer, Direction.RIGHT, [(0, 0), (1, 0)]),
])
def test_ship_coordinate_generation(ship: Ship, direction: Direction, expected):
    assert ship.generate_ship_coordinates((0, 0), direction) == expected
