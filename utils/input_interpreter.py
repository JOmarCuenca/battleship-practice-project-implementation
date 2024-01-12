from . import logger
from errors.input_exceptions import *
from constants.str_coordinates import StringCoordinate
from constants.directions import Direction


class InputInterperter:

    @logger.catch(reraise=True)
    def coord_to_tuple(self, coord: str):
        """
        Converts a string coordinate to a tuple coordinate
        """
        if not 2 <= len(coord) <= 3:
            raise InvalidCoordInputException(coord)

        letter_axis = None

        try:
            letter_axis = StringCoordinate[coord[0]]
        except KeyError as e:
            raise InvalidStrAxisException(coord[0]) from e

        number_axis = None

        try:
            number_axis = int(coord[1:])
            if not 1 <= number_axis <= 10:
                raise InvalidNumericAxisException(coord[1:])
        except ValueError as e:
            raise InvalidNumericAxisException(coord[1:]) from e

        return (letter_axis.value, number_axis - 1)

    def generate_ship_coordinates(self, start_coordinate: str, direction: Direction, size: int):
        """
        Generates a list of coordinates for a ship
        """
        start_coordinate = self.coord_to_tuple(start_coordinate)
        ship_coordinates = []

        for i in range(size):
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
    
    @logger.catch(reraise=True)
    def get_direction(self, dir: str) -> Direction:
        """
        Converts a string direction to a Direction enum
        """
        try:
            return Direction[dir.upper()]
        except KeyError as e:
            raise InvalidDirectionException(dir) from e
