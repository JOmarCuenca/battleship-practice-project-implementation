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
    ([(-1, 0)], InvalidShipPlacementException), # x < 0
    ([(0, -1)], InvalidShipPlacementException), # y < 0
    ([(10, 0)], InvalidShipPlacementException), # x > 9
    ([(0, 10)], InvalidShipPlacementException), # y > 9
    ([(0, 0), (0, 0)], OverlappedShipException), # overlapped ships
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

    assert all(isinstance(coordinate, ShipCoordinate) for row in board.coordinates for coordinate in row)
