import pygame
from snake import Snake

class Game:
    def __init__(self):
        # settings
        WINDOW_WIDTH_AND_HIGHT = 600
        self.FPS = 5
        self.BACKGROUND_COLOR = (30, 30, 30)
        self.cell_amount = 20
        
        # init window
        self.WINDOW = pygame.display.set_mode((WINDOW_WIDTH_AND_HIGHT, WINDOW_WIDTH_AND_HIGHT))
        pygame.display.set_caption("Snakepy")

        # init game
        self.cell_size = self.WINDOW.get_width() / self.cell_amount
        self.CLOCK = pygame.time.Clock()
        self.snake = Snake(self)

    def run(self):
        self.CLOCK.tick(self.FPS)

        self.snake.update()

        self.update_graphics()
    
    def update_graphics(self):
        self.WINDOW.fill(self.BACKGROUND_COLOR)

        self.snake.draw(self.WINDOW)

        pygame.display.flip()