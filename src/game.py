import pygame
import random
from rect_sprite import RectSprite
from game_settings import GameSettings
from events import Events

class Game:
    def __init__(self) -> None:
        from snake import Snake
        # init window
        wwh = GameSettings.WINDOW_WIDTH_AND_HIGHT
        self.WINDOW = pygame.display.set_mode((wwh, wwh))
        pygame.display.set_caption("Snakepy")

        # init game
        self.cell_size = self.WINDOW.get_width() / GameSettings.CELL_AMOUNT
        self.CLOCK = pygame.time.Clock()
        self.delta_time = 0
        self.running = True
        self.snake = Snake(self)
        self.score = 0
        self.FONT = pygame.font.SysFont("calibri", 32)

        self.fruit_group = pygame.sprite.GroupSingle()
        self._spawn_fruit()

    def run(self) -> None:
        if self.running:
            self.delta_time = self.CLOCK.tick(GameSettings.FPS)
            self.snake.update()

        self._update_graphics()

        if not self.running:
            self._check_restart()
    
    def end_game(self) -> None:
        self.running = False

    def _update_graphics(self) -> None:
        self.WINDOW.fill(GameSettings.BACKGROUND_COLOR)

        self.snake.draw(self.WINDOW)
        self.fruit_group.draw(self.WINDOW)
        self._draw_score()

        if not self.running: self._draw_game_over()

        pygame.display.flip()
    
    def _spawn_fruit(self) -> None:

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

        self.fruit_group.add(RectSprite(size, (pos_x, pos_y), GameSettings.FRUIT_COLOR))
    
    def _draw_score(self):
        self.WINDOW.blit(self.FONT.render(str(self.score), True, GameSettings.TEXT_COLOR), (self.WINDOW.get_width() / 2, 50))
    
    def _draw_game_over(self):
        game_over_text = "Game Over"
        score_text = "Score: " + str(self.score)
        restart_text = "Press Enter to restart"

        title_width = self.FONT.size(game_over_text)[0]
        score_width = self.FONT.size(score_text)[0]
        restart_width = self.FONT.size(restart_text)[0]

        self.WINDOW.blit(self.FONT.render(game_over_text, True, (255, 50, 50)),
            (self.WINDOW.get_width() / 2 - title_width / 2, self.WINDOW.get_height() / 2 - 48))
        self.WINDOW.blit(self.FONT.render(score_text, True, (255, 255, 255)),
            (self.WINDOW.get_width() / 2 - score_width / 2, self.WINDOW.get_height() / 2))
        self.WINDOW.blit(self.FONT.render(restart_text, True, (255, 255, 255)),
            (self.WINDOW.get_width() / 2 - restart_width / 2, self.WINDOW.get_height() / 2 + 48)
        )
    
    def _check_restart(self):
        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[pygame.K_RETURN]:
            pygame.event.post(pygame.event.Event(Events.RESTART))