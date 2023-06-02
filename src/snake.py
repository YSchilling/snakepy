import pygame
from snake_head import SnakeHead
from direction import Direction

class Snake:
    def __init__(self, game):
        self.game = game
        
        self.head_group = pygame.sprite.GroupSingle()
        size = (game.cell_size, game.cell_size)
        middle_coords = game.cell_size * (game.cell_amount / 2)
        pos = (middle_coords, middle_coords)
        self.head_group.add(SnakeHead(size, pos, (0, 255, 0)))
    
    def update(self):
        self.head_group.update()
        self._move()

    def draw(self, surface):
        self.head_group.draw(surface)
    
    def _move(self):
        snake_head = self.head_group.sprite

        if snake_head.direction == Direction.UP:
            snake_head.rect.y -= self.game.cell_size
        elif snake_head.direction == Direction.RIGHT:
            snake_head.rect.x += self.game.cell_size
        elif snake_head.direction == Direction.DOWN:
            snake_head.rect.y += self.game.cell_size
        elif snake_head.direction == Direction.LEFT:
            snake_head.rect.x -= self.game.cell_size