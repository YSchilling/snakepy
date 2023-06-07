import pygame

class RectSprite(pygame.sprite.Sprite):
    def __init__(self, size: tuple[int, int], pos: tuple[int, int], color: tuple[int, int, int]):
        super().__init__()

        self.image: pygame.surface.Surface = pygame.surface.Surface(size)
        self.image.fill(color)
        self.rect: pygame.rect.Rect = self.image.get_rect()
        self.rect.topleft = pos