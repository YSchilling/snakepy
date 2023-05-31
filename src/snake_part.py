import pygame

class SnakePart(pygame.sprite.Sprite):
    def __init__(self, size, pos, color):
        super().__init__()

        self.image = pygame.surface.Surface(size)
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.topleft = pos