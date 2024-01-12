class InvalidInputException(Exception):
    pass


class InvalidCoordInputException(InvalidInputException):

    def __init__(self, coordinate_string):
        self.coordinate_string = coordinate_string

    def __str__(self):
        return f"Coordinate {self.coordinate_string} isn't a valid coordinate. Please enter a valid coordinate like A1 or J10."


class InvalidStrAxisException(InvalidInputException):

    def __init__(self, axis):
        self.axis = axis

    def __str__(self):
        return f"Axis {self.axis} isn't a valid axis. Please enter a valid axis, A-J."


class InvalidNumericAxisException(InvalidInputException):

    def __init__(self, axis):
        self.axis = axis

    def __str__(self):
        return f"Axis {self.axis} isn't a valid axis. Please enter a valid axis, 1 - 9."


class InvalidDirectionException(InvalidInputException):
    
        def __init__(self, direction):
            self.direction = direction
    
        def __str__(self):
            return f"Direction {self.direction} isn't a valid direction. Please enter a valid direction, up, down, left, right."
