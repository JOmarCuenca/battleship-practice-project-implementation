from classes.board import Board
from classes.coordinate import Coordinate, ShipCoordinate
from errors.board_exceptions import InvalidShipPlacementException, OverlappedShipException

import pytest


def test_empty_board_creation():
    new_board = Board()

    assert len(new_board.coordinates) == 10

    for row in new_board.coordinates:
        assert len(row) == 10
        assert all(isinstance(coordinate, Coordinate) for coordinate in row)


@pytest.mark.parametrize("coordinates, expected_exception", [
    ([(-1, 0)], InvalidShipPlacementException),  # x < 0
    ([(0, -1)], InvalidShipPlacementException),  # y < 0
    ([(10, 0)], InvalidShipPlacementException),  # x > 9
    ([(0, 10)], InvalidShipPlacementException),  # y > 9
    ([(0, 0), (0, 0)], OverlappedShipException),  # overlapped ships
])
def test_invalid_ship_placement(coordinates: list[tuple[int, int]], expected_exception):
    board = Board()

    with pytest.raises(expected_exception):
        board.place_ship(coordinates)


def test_valid_ship_placement():
    board = Board()

    for x in range(10):
        for y in range(10):
            board.place_ship([(x, y)])

    assert all(isinstance(coordinate, ShipCoordinate)
               for row in board.coordinates for coordinate in row)


@pytest.mark.parametrize("coords, expected_board_file", [
    ([], 'tests/examples/empty_board.out'),
    ([
        (x, 2) for x in range(2, 6)
    ], 'tests/examples/1_boat_board_1.out'),  # Horizontal Small boat on middle low
    ([
        (0, x) for x in range(5)
    ], 'tests/examples/1_boat_board_2.out'),  # Vertical Small boat on left-bottom corner
    ([
        (x, 9) for x in range(10)
    ], 'tests/examples/1_boat_board_3.out'),  # Horizontal Large Boat on top row
    (
        [(x, 2) for x in range(2, 7)] +
        [(x, 7) for x in range(2, 7)] +
        [(2, y) for y in range(3, 7)] +
        [(6, y) for y in range(3, 7)] +
        [(4, 4), (4, 5)], 'tests/examples/multi_boats_square.out'
    )  # Square shaped formation
])
def test_player_board_print(coords, expected_board_file: str):
    board = Board()

    board.place_ship(coords)

    with open(expected_board_file) as f:
        expected_board = f.read()

    assert '\n'.join(board.player_lines()) == expected_board
