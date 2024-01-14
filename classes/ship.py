from constants.directions import Direction


class Ship:
    size: int = 0

    @classmethod
    def generate_ship_coordinates(cls, start_coordinate: tuple[int, int], direction: Direction) -> list[tuple[int, int]]:
        """
        Generates a list of coordinates for a ship
        """
        ship_coordinates = []

        for i in range(cls.size):
            if direction == Direction.UP:
                ship_coordinates.append(
                    (start_coordinate[0], start_coordinate[1] + i))
            elif direction == Direction.DOWN:
                ship_coordinates.append(
                    (start_coordinate[0], start_coordinate[1] - i))
            elif direction == Direction.LEFT:
                ship_coordinates.append(
                    (start_coordinate[0] - i, start_coordinate[1]))
            elif direction == Direction.RIGHT:
                ship_coordinates.append(
                    (start_coordinate[0] + i, start_coordinate[1]))

        return ship_coordinates


class Carrier(Ship):
    size: int = 5


class Battleship(Ship):
    size: int = 4


class Cruiser(Ship):
    size: int = 3


class Submarine(Ship):
    size: int = 3


class Destroyer(Ship):
    size: int = 2


SHIPS_PER_GAME = [Carrier(), Battleship(), Cruiser(), Submarine(), Destroyer()]
