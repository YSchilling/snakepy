import pygame

class Game:
    def __init__(self):
        # settings
        WINDOW_WIDTH, WINDOW_HEIGHT = 600, 600
        
        
        self.WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))