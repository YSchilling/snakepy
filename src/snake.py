import pygame
from snake_head import SnakeHead
from direction import Direction

class Snake:
    def __init__(self, game):
        # settings
        self.game = game
        self.moves_per_second = 1.5

        # init
        self.head_group = pygame.sprite.GroupSingle()
        size = (game.cell_size, game.cell_size)
        middle_coords = game.cell_size * (game.cell_amount / 2)
        pos = (middle_coords, middle_coords)
        self.head_group.add(SnakeHead(size, pos, (0, 255, 0)))

        self.move_timer = 0
    
    def update(self):
        self.head_group.update()
        if self._is_time_to_move():
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
    
    def _is_time_to_move(self):
        self.move_timer += self.game.delta_time

        if self.move_timer > (1000 / self.moves_per_second):
            self.move_timer = 0
            return True
        
        return False