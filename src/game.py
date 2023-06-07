import pygame
import random
from snake import Snake
from fruit import Fruit

class Game:
    def __init__(self):
        # settings
        WINDOW_WIDTH_AND_HIGHT = 600
        self.FPS = 60
        self.BACKGROUND_COLOR = (30, 30, 30)
        self.cell_amount = 20
        self.SNAKE_HEAD_COLOR = (0, 200, 0)
        self.SNAKE_TAIL_COLOR = (0, 255, 0)
        
        # init window
        self.WINDOW = pygame.display.set_mode((WINDOW_WIDTH_AND_HIGHT, WINDOW_WIDTH_AND_HIGHT))
        pygame.display.set_caption("Snakepy")

        # init game
        self.cell_size = self.WINDOW.get_width() / self.cell_amount
        self.CLOCK = pygame.time.Clock()
        self.delta_time = 0
        self.running = True
        self.snake = Snake(self)

        self.fruit_group = pygame.sprite.GroupSingle()
        self._spawn_fruit()

    def run(self):
        self.delta_time = self.CLOCK.tick(self.FPS)

        self.snake.update()

        self._update_graphics()
    
    def end_game(self):
        self.running = False

    def _update_graphics(self):
        self.WINDOW.fill(self.BACKGROUND_COLOR)

        self.snake.draw(self.WINDOW)
        self.fruit_group.draw(self.WINDOW)

        pygame.display.flip()
    
    def _spawn_fruit(self):

        found_empty_cell = False
        while not found_empty_cell:
            pos_x_list = [x for x in range(0, self.WINDOW.get_width(), int(self.cell_size))]
            pos_y_list = [y for y in range(0, self.WINDOW.get_height(), int(self.cell_size))]

            pos_x = random.choice(pos_x_list)
            pos_y = random.choice(pos_y_list)
            size = (self.cell_size, self.cell_size)

            test_rect = pygame.rect.Rect((pos_x, pos_y), size)
            if (
                test_rect.collidelist(self.snake.tail_group.sprites()) == -1
                and test_rect.collidelist(self.snake.head_group.sprites()) == -1
            ):
                found_empty_cell = True

        self.fruit_group.add(Fruit(size, (pos_x, pos_y), (153, 153, 255)))