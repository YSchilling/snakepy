import pygame

class Game:
    def __init__(self):
        # settings
        WINDOW_WIDTH, WINDOW_HEIGHT = 600, 600
        self.FPS = 60
        
        # init window
        self.WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

        # init game
        self.CLOCK = pygame.time.Clock()

    def run(self):
        self.CLOCK.tick(self.FPS)