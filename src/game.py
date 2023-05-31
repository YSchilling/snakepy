import pygame
from snake import Snake

class Game:
    def __init__(self):
        # settings
        WINDOW_WIDTH, WINDOW_HEIGHT = 600, 600
        self.FPS = 60
        self.BACKGROUND_COLOR = (30, 30, 30)
        
        # init window
        self.WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Snakepy")

        # init game
        self.CLOCK = pygame.time.Clock()
        self.snake = Snake()

    def run(self):
        self.CLOCK.tick(self.FPS)

        self.snake.update()

        self.update_graphics()
    
    def update_graphics(self):
        self.WINDOW.fill(self.BACKGROUND_COLOR)

        self.snake.draw(self.WINDOW)

        pygame.display.flip()