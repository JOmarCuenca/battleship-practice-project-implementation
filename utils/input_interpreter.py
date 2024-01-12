from . import logger
from errors.input_exceptions import *
from constants.str_coordinates import StringCoordinate
from constants.directions import Direction


class InputInterperter:

    def coord_to_tuple(self, coord: str):
        """
        Converts a string coordinate to a tuple coordinate
        """
        if not 2 <= len(coord) <= 3:
            raise InvalidCoordInputException(coord)

        coord = coord.upper()

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

    def get_direction(self, dir: str) -> Direction:
        """
        Converts a string direction to a Direction enum
        """
        try:
            return Direction[dir.upper()]
        except KeyError as e:
            raise InvalidDirectionException(dir) from e
