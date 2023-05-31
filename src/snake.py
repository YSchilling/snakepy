import pygame
from snake_head import SnakeHead
from direction import Direction

class Snake:
    def __init__(self):
        self.head_group = pygame.sprite.GroupSingle()
        self.head_group.add(SnakeHead((20, 20), (200, 200), (0, 255, 0)))
    
    def update(self):
        self.head_group.update()
        self._move()

    def draw(self, surface):
        self.head_group.draw(surface)
    
    def _move(self):
        snake_head = self.head_group.sprite

        if snake_head.direction == Direction.UP:
            snake_head.rect.y -= 1
        elif snake_head.direction == Direction.RIGHT:
            snake_head.rect.x += 1
        elif snake_head.direction == Direction.DOWN:
            snake_head.rect.y += 1
        elif snake_head.direction == Direction.LEFT:
            snake_head.rect.x -= 1