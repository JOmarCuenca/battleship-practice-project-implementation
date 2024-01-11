from . import logger
from errors.input_exceptions import InvalidCoordInputException, InvalidStrAxisException, InvalidNumericAxisException
from constants.str_coordinates import StringCoordinate

class InputInterperter:
    
    @logger.catch(reraise=True)
    def coord_to_tuple(self, coord : str):
        """
        Converts a string coordinate to a tuple coordinate
        """
        if len(coord) != 2:
            raise InvalidCoordInputException(coord)
        
        letter_axis = None
        
        try:
            letter_axis = StringCoordinate[coord[0]]
        except KeyError as e:
            raise InvalidStrAxisException(coord[0]) from e
        
        number_axis = None

        try:
            number_axis = int(coord[1])
        except ValueError as e:
            raise InvalidNumericAxisException(coord[1]) from e
        
        return (letter_axis.value, number_axis)
        



        
