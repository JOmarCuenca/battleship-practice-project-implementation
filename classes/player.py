import random
from classes.board import Board
from classes.coordinate import ShipCoordinate
from classes.ship import Ship
from constants.directions import Direction
from errors.game_exceptions import DuplicateCoordException, InvalidAttackCoordException
from utils import logger
from utils.input_interpreter import InputInterperter


class Player:
    name: str = "Player"
    board: Board
    boats_placed: bool = False

    def __init__(self):
        self.reset_board()

    def set_board(self, board: Board):
        self.board = board
        logger.debug(f"Board set for {self.name}")

    def reset_board(self):
        self.set_board(Board())
        self.boats_placed = False
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

        try:
            coord = self.board.coordinates[attacked_coord[1]][attacked_coord[0]]
        except IndexError:
            raise InvalidAttackCoordException(attacked_coord) from IndexError

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

    def __str__(self):
        return self.name


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

    def __init__(self, surname: str = ""):
        super().__init__()
        self.name = f"{self.name} {surname}"

    def pick_coordinate(self) -> tuple[int, int]:
        return (random.randint(0, 9), random.randint(0, 9))

    def pick_direction(self) -> Direction:
        return random.choice(list(Direction))


class BeginnerComputerPlayer(ComputerPlayer):
    name: str = "Random Computer"


class SmartComputerPlayer(ComputerPlayer):
    name: str = "Expert Computer"

    target_coord: tuple[int, int] = (0, 0)

    hit_coords: set[tuple[int, int]] = set()
    boat_probable_coords: list[tuple[int, int]] = []

    def pick_coordinate(self) -> tuple[int, int]:
        if self.boats_placed and self.boat_probable_coords:
            self.target_coord = random.choice(self.boat_probable_coords)
            self.boat_probable_coords.remove(self.target_coord)

        else:
            self.target_coord = super().pick_coordinate()

            while self.target_coord in self.hit_coords:
                self.target_coord = super().pick_coordinate()
            
        return self.target_coord

    def attack(self, opponent) -> bool:
        hit = super().attack(opponent)

        self.hit_coords.add(self.target_coord)

        if hit:
            self.boat_probable_coords.extend([
                (self.target_coord[0] + 1, self.target_coord[1]),
                (self.target_coord[0] - 1, self.target_coord[1]),
                (self.target_coord[0], self.target_coord[1] + 1),
                (self.target_coord[0], self.target_coord[1] - 1),
            ])
            

        return hit
