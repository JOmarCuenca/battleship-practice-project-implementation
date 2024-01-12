from dataclasses import dataclass

from classes.coordinate import Coordinate, ShipCoordinate
from errors.board_exceptions import InvalidShipPlacementException, OverlappedShipException
from utils import logger

BOARD_SIZE = 10


@dataclass(eq=True)
class Board:
    coordinates: list[list[Coordinate]]

    def __init__(self):
        self.coordinates = [[Coordinate(x, y) for x in range(
            BOARD_SIZE)] for y in range(BOARD_SIZE)]

    @staticmethod
    def board_line():
        return '+'.join(['-' * 3] * BOARD_SIZE)

    @staticmethod
    def player_view_row(row: list[Coordinate]):
        return '|'.join([coordinate.player_view_char().center(3) for coordinate in row])

    @staticmethod
    def opponent_view_row(row: list[Coordinate]):
        return '|'.join([coordinate.opponent_view_char().center(3) for coordinate in row])

    def player_lines(self):
        result = []

        for row in self.coordinates:
            result.append(self.player_view_row(row))
            result.append(self.board_line())

        result.pop()

        return result

    def opponent_lines(self):
        result = []

        for row in self.coordinates:
            result.append(self.opponent_view_row(row))
            result.append(self.board_line())

        result.pop()

        return result

    @logger.catch(reraise=True)
    def place_ship(self, ship: list[tuple[int, int]]):
        newly_placed_coordinates = set()

        for coordinate in ship:
            x, y = coordinate

            if not (0 <= x <= 9 and 0 <= y <= 9):
                raise InvalidShipPlacementException(coordinate)

            try:
                if isinstance(self.coordinates[y][x], ShipCoordinate) or coordinate in newly_placed_coordinates:
                    raise OverlappedShipException(coordinate)

                newly_placed_coordinates.add(coordinate)
            except IndexError as e:
                raise InvalidShipPlacementException(coordinate) from e

        for coordinate in ship:
            x, y = coordinate
            self.coordinates[y][x] = ShipCoordinate(x, y)
