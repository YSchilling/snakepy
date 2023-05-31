import pygame
from snake_head import SnakeHead

class Snake:
    def __init__(self):
        self.head_group = pygame.sprite.GroupSingle()
        self.head_group.add(SnakeHead((20, 20), (200, 200), (0, 255, 0)))
    
    def draw(self, surface):
        self.head_group.draw(surface)