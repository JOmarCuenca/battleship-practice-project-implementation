class InvalidCoordInputException(Exception):

    def __init__(self, coordinate_string):
        self.coordinate_string = coordinate_string

    def __str__(self):
        return f"Coordinate {self.coordinate_string} isn't a valid coordinate. Please enter a coordinate with two characters, like (A1)."


class InvalidStrAxisException(Exception):

    def __init__(self, axis):
        self.axis = axis

    def __str__(self):
        return f"Axis {self.axis} isn't a valid axis. Please enter a valid axis, A-J."


class InvalidNumericAxisException(Exception):

    def __init__(self, axis):
        self.axis = axis

    def __str__(self):
        return f"Axis {self.axis} isn't a valid axis. Please enter a valid axis, 1 - 9."
