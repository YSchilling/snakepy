import pygame

class Game:
    def __init__(self):
        # settings
        WINDOW_WIDTH, WINDOW_HEIGHT = 600, 600
        self.FPS = 60
        self.BACKGROUND_COLOR = (30, 30, 30)
        
        # init window
        self.WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

        # init game
        self.CLOCK = pygame.time.Clock()

    def run(self):
        self.CLOCK.tick(self.FPS)

        self.update_graphics()
    
    def update_graphics(self):
        self.WINDOW.fill(self.BACKGROUND_COLOR)

        pygame.display.flip()