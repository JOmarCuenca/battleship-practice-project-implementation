class GameBoardException(Exception):
    """Base class for exceptions in this module."""
    pass

class OverlappedShipException(GameBoardException):
    """Exception raised when a ship is placed on top of another ship"""
    
    def __init__(self, coordinate: tuple[int, int]):
        self.coordinate = coordinate

    def __str__(self):
        return f"Ship placed on top of another ship at {self.coordinate}"
    
class InvalidShipPlacementException(GameBoardException):
    """Exception raised when a ship is placed outside the board"""
    
    def __init__(self, coordinate: tuple[int, int]):
        self.coordinate = coordinate

    def __str__(self):
        return f"Ship placed outside the board at {self.coordinate}"