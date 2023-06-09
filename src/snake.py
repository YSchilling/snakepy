import pygame
from snake_head import SnakeHead
from rect_sprite import RectSprite
from direction import Direction
from game import Game
from game_settings import GameSettings

class Snake:
    def __init__(self, game: Game) -> None:
        self.game = game
        self.moves_per_second = GameSettings.MOVES_PER_SECOND
        self.move_timer = 0
        self.append_tail = False

        self.head_group = pygame.sprite.GroupSingle()
        middle_coords = game.cell_size[0] * (GameSettings.CELL_AMOUNT / 2)
        pos = (middle_coords, middle_coords)
        self.head_group.add(SnakeHead(game.cell_size, pos, GameSettings.SNAKE_HEAD_COLOR))

        self.tail_group = pygame.sprite.Group()
        for i in range(1, 5):
            pos = (middle_coords, middle_coords + i*game.cell_size[0])
            self.tail_group.add(RectSprite(self.game.cell_size, pos, GameSettings.SNAKE_TAIL_COLOR))
    
    def update(self) -> None:
        self.head_group.update()

        if self._is_time_to_move():
            if self._is_cell_ahead_valid():
                self._move()
            else:
                self.game.end_game()
            
        self._check_fruit_collision()

    def draw(self, surface: pygame.surface.Surface) -> None:
        self.head_group.draw(surface)
        self.tail_group.draw(surface)
    
    def _move(self) -> None:
        snake_head = self.head_group.sprite
        snake_head.update_last_moved_direction()

        snake_part_positions = [snake_head.rect.topleft] + [tail.rect.topleft for tail in self.tail_group]
        
        # move head
        if snake_head.direction == Direction.UP:
            snake_head.rect.y -= self.game.cell_size[1]
        elif snake_head.direction == Direction.RIGHT:
            snake_head.rect.x += self.game.cell_size[0]
        elif snake_head.direction == Direction.DOWN:
            snake_head.rect.y += self.game.cell_size[1]
        elif snake_head.direction == Direction.LEFT:
            snake_head.rect.x -= self.game.cell_size[0]
        
        # move tail
        for i, tail in enumerate(self.tail_group):
            tail.rect.topleft = snake_part_positions[i]
        
        if self.append_tail:
            last_pos = snake_part_positions[-1]
            new_tail = RectSprite(self.game.cell_size, last_pos, GameSettings.SNAKE_TAIL_COLOR)
            self.tail_group.add(new_tail)
            self.append_tail = False
        
    def _is_time_to_move(self) -> None:
        self.move_timer += self.game.delta_time

        if self.move_timer > (1000 / self.moves_per_second):
            self.move_timer = 0
            return True
        
        return False
    
    def _is_cell_ahead_valid(self) -> None:
        if self._is_cell_ahead_in_board() and self._is_cell_ahead_empty():
            return True
        return False
    
    def _is_cell_ahead_in_board(self) -> None:
        head = self.head_group.sprite
        head_pos_x, head_pos_y = head.rect.center
        cell_size = self.game.cell_size[0]

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
    
    def _is_cell_ahead_empty(self) -> None:
        head = self.head_group.sprite
        cell_size = self.game.cell_size[0]

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
        test_rect = pygame.rect.Rect(cell_ahead, self.game.cell_size)
        if test_rect.collidelist(tails) == -1:
            return True
        return False
    
    def _check_fruit_collision(self) -> None:
        head = self.head_group.sprite
        fruit = self.game.fruit_group.sprite

        if head.rect.colliderect(fruit.rect):
            fruit.kill()
            self.append_tail = True
            self.game.score += 1
            self.game._spawn_fruit()