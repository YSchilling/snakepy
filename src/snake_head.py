from snake_part import SnakePart
from direction import Direction

class SnakeHead(SnakePart):
    def __init__(self, size, pos, color):
        super().__init__(size, pos, color)

        self.direction = Direction.UP