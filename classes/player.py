from classes.board import Board
from classes.coordinate import ShipCoordinate
from classes.ship import Ship
from constants.directions import Direction
from errors.game_exceptions import DuplicateCoordException
from utils import logger
from utils.input_interpreter import InputInterperter


class Player:
    name: str = "Player"
    board: Board

    def __init__(self):
        self.reset_board()

    def set_board(self, board: Board):
        self.board = board
        logger.debug(f"Board set for {self.name}")

    def reset_board(self):
        self.set_board(Board())
        logger.debug(f"Board reset for {self.name}")

    def has_lost(self) -> bool:
        for row in self.board.coordinates:
            for coordinate in row:
                if isinstance(coordinate, ShipCoordinate) and not coordinate.hit:
                    return False
        return True

    def pick_coordinate(self) -> tuple[int, int]:
        raise NotImplementedError()

    def pick_direction(self) -> Direction:
        raise NotImplementedError()

    def attack(self, opponent) -> bool:
        coord = self.pick_coordinate()
        logger.debug(f"{self.name} picked {coord} to attack")
        return opponent.defend(coord)

    def defend(self, attacked_coord: tuple[int, int]) -> bool:
        logger.debug(f"{self.name} is was attacked at {attacked_coord}")

        coord = self.board.coordinates[attacked_coord[1]][attacked_coord[0]]

        if coord.hit:
            raise DuplicateCoordException(attacked_coord)

        coord.hit = True

        return isinstance(coord, ShipCoordinate)

    def place_ship(self, ship: Ship) -> list[tuple[int, int]]:
        logger.debug(f"{self.name} is placing {ship.__class__.__name__}")

        coord = self.pick_coordinate()
        logger.debug(f"{self.name} picked {coord}")
        direction = self.pick_direction()
        logger.debug(f"{self.name} picked {direction}")

        ship_coordinates = ship.generate_ship_coordinates(coord, direction)

        self.board.place_ship(ship_coordinates)

        logger.debug("Ship placed")

        return ship_coordinates


class HumanPlayer(Player):
    name: str = "Human"
    interpreter = InputInterperter()

    def pick_coordinate(self) -> tuple[int, int]:
        user_input = input("Pick a coordinate (e.g. A1): ")
        return self.interpreter.coord_to_tuple(user_input)

    def pick_direction(self) -> Direction:
        user_input = input("Pick a direction (e.g. right): ")
        return self.interpreter.get_direction(user_input)


class ComputerPlayer(Player):
    name: str = "Computer"

import random

class EasyComputerPlayer(ComputerPlayer):
    name: str = "Easy Computer"

    def pick_coordinate(self) -> tuple[int, int]:
        return (random.randint(0, 9), random.randint(0, 9))

    def pick_direction(self) -> Direction:
        return random.choice(list(Direction))
