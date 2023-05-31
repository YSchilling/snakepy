import pygame
from snake_part import SnakePart
from direction import Direction

class SnakeHead(SnakePart):
    def __init__(self, size, pos, color):
        super().__init__(size, pos, color)

        self.direction = Direction.UP
    
    def update(self):
        self._update_direction()
    
    def _update_direction(self):
        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[pygame.K_UP] and self.direction != Direction.DOWN:
            self.direction = Direction.UP
        if keys_pressed[pygame.K_RIGHT] and self.direction != Direction.LEFT:
            self.direction = Direction.RIGHT
        if keys_pressed[pygame.K_DOWN] and self.direction != Direction.UP:
            self.direction = Direction.DOWN
        if keys_pressed[pygame.K_LEFT] and self.direction != Direction.RIGHT:
            self.direction = Direction.LEFT