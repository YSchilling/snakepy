import pygame
from snake import Snake

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
        self.snake = Snake(self)
        self.delta_time = 0
        self.running = True

    def run(self):
        self.delta_time = self.CLOCK.tick(self.FPS)

        self.snake.update()

        self._update_graphics()
    
    def end_game(self):
        self.running = False

    def _update_graphics(self):
        self.WINDOW.fill(self.BACKGROUND_COLOR)

        self.snake.draw(self.WINDOW)

        pygame.display.flip()