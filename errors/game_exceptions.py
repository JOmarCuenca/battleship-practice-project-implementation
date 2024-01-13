class GameplayException(Exception):
    """Base class for exceptions in this module."""
    pass

class DuplicateCoordException(GameplayException):

    def __init__(self, coord: tuple[int, int]):
        self.coord = coord

    def __str__(self):
        return f"Coordinate {self.coord} has been picked before"
    
class InvalidAttackCoordException(GameplayException):
    def __init__(self, coord: tuple[int, int]):
        self.coord = coord

    def __str__(self):
        return f"Coordinate {self.coord} is invalid"