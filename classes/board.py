from dataclasses import dataclass

from .coordinate import Coordinate, ShipCoordinate

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
