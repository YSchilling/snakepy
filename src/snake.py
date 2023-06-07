import pygame
from snake_head import SnakeHead
from rect_sprite import RectSprite
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
        self.head_group.add(SnakeHead(size, pos, game.SNAKE_HEAD_COLOR))

        self.tail_group = pygame.sprite.Group()
        for i in range(1, 5):
            pos = (middle_coords, middle_coords + i*game.cell_size)
            self.tail_group.add(RectSprite(size, pos, game.SNAKE_TAIL_COLOR))

        self.move_timer = 0
        self.append_tail = False
    
    def update(self):
        self.head_group.update()
        if self._is_time_to_move() and self.game.running:
            if not self._is_cell_ahead_valid():
                self.game.end_game()
            self._move()
        self._check_fruit_collision()

    def draw(self, surface):
        self.head_group.draw(surface)
        self.tail_group.draw(surface)
    
    def _move(self):
        snake_head = self.head_group.sprite

        snake_part_positions = [snake_head.rect.topleft] + [tail.rect.topleft for tail in self.tail_group]
        
        # move head
        if snake_head.direction == Direction.UP:
            snake_head.rect.y -= self.game.cell_size
        elif snake_head.direction == Direction.RIGHT:
            snake_head.rect.x += self.game.cell_size
        elif snake_head.direction == Direction.DOWN:
            snake_head.rect.y += self.game.cell_size
        elif snake_head.direction == Direction.LEFT:
            snake_head.rect.x -= self.game.cell_size
        
        # move tail
        for i, tail in enumerate(self.tail_group):
            tail.rect.topleft = snake_part_positions[i]
        
        if self.append_tail:
            last_pos = snake_part_positions[-1]
            pos = (last_pos[0], last_pos[1])
            size = (self.game.cell_size, self.game.cell_size)
            new_tail = RectSprite(size, pos, self.game.SNAKE_TAIL_COLOR)
            self.tail_group.add(new_tail)
            self.append_tail = False
        
    def _is_time_to_move(self):
        self.move_timer += self.game.delta_time

        if self.move_timer > (1000 / self.moves_per_second):
            self.move_timer = 0
            return True
        
        return False
    
    def _is_cell_ahead_valid(self):
        if self._is_cell_ahead_in_board() and self._is_cell_ahead_empty():
            return True
        return False
    
    def _is_cell_ahead_in_board(self):
        head = self.head_group.sprite
        head_pos_x, head_pos_y = head.rect.center
        cell_size = self.game.cell_size

        if head.direction == Direction.UP:
            if (head_pos_y - cell_size) < 0:
                return False
        elif head.direction == Direction.RIGHT:
            if (head_pos_x + cell_size) > self.game.WINDOW.get_width():
                return False
        elif head.direction == Direction.DOWN:
            if (head_pos_y + cell_size) > self.game.WINDOW.get_height():
                return False
        elif head.direction == Direction.LEFT:
            if (head_pos_x - cell_size) < 0:
                return False
        
        return True
    
    def _is_cell_ahead_empty(self):
        head = self.head_group.sprite
        cell_size = self.game.cell_size

        # define the cell ahead to test collision
        if head.direction == Direction.UP:
            cell_ahead = (head.rect.x, head.rect.y - cell_size)
        elif head.direction == Direction.RIGHT:
            cell_ahead = (head.rect.x + cell_size, head.rect.y)
        elif head.direction == Direction.DOWN:
            cell_ahead = (head.rect.x, head.rect.y + cell_size)
        elif head.direction == Direction.LEFT:
            cell_ahead = (head.rect.x - cell_size, head.rect.y)
        
        tails = self.tail_group.sprites()
        test_rect = pygame.rect.Rect(cell_ahead, (cell_size, cell_size))
        if test_rect.collidelist(tails) == -1:
            return True
        return False
    
    def _check_fruit_collision(self):
        head = self.head_group.sprite
        fruit = self.game.fruit_group.sprite

        if head.rect.colliderect(fruit.rect):
            fruit.kill()
            self.append_tail = True
            self.game._spawn_fruit()