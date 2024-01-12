from dataclasses import dataclass


@dataclass(eq=True)
class Coordinate:
    x: int
    y: int
    hit: bool = False

    def opponent_view_char(self):
        if self.hit:
            return '.'
        else:
            return ' '

    def player_view_char(self):
        if self.hit:
            return '.'
        else:
            return ' '


class ShipCoordinate(Coordinate):

    def create_from_coordinate(coordinate):
        return ShipCoordinate(coordinate.x, coordinate.y, coordinate.hit)

    def opponent_view_char(self):
        if self.hit:
            return 'X'
        else:
            return ' '

    def player_view_char(self):
        if self.hit:
            return 'X'
        else:
            return 'B'
