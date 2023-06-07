import pygame
from direction import Direction
from rect_sprite import RectSprite

class SnakeHead(RectSprite):
    def __init__(self, size: tuple[int, int], pos: tuple[int, int], color: tuple[int, int, int]) -> None:
        super().__init__(size, pos, color)

        self.direction = Direction.UP
        self.last_moved_direction = self.direction
    
    def update(self) -> None:
        self._update_direction()
    
    def update_last_moved_direction(self) -> None:
        self.last_moved_direction = self.direction
    
    def _update_direction(self) -> None:
        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[pygame.K_UP] and self.last_moved_direction != Direction.DOWN:
            self.direction = Direction.UP
        if keys_pressed[pygame.K_RIGHT] and self.last_moved_direction != Direction.LEFT:
            self.direction = Direction.RIGHT
        if keys_pressed[pygame.K_DOWN] and self.last_moved_direction != Direction.UP:
            self.direction = Direction.DOWN
        if keys_pressed[pygame.K_LEFT] and self.last_moved_direction != Direction.RIGHT:
            self.direction = Direction.LEFT