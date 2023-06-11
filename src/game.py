import pygame
import random
from rect_sprite import RectSprite
from game_settings import GameSettings
from events import Events
from scoreboard import Scoreboard

class Game:
    def __init__(self) -> None:
        from snake import Snake
        # init window
        self.WINDOW = pygame.display.set_mode((GameSettings.WINDOW_WIDTH_AND_HIGHT, GameSettings.WINDOW_WIDTH_AND_HIGHT))
        pygame.display.set_caption("Snakepy")

        # init game
            # constants
        self.CLOCK = pygame.time.Clock()
        self.FONT = pygame.font.SysFont("calibri", 28)

            # attributes
        cell_width = int(self.WINDOW.get_width() / GameSettings.CELL_AMOUNT)
        self.cell_size = (cell_width, cell_width)
        self.delta_time = 0
        self.running = True
        self.score = 0
        self.scoreboard = Scoreboard(GameSettings.SCOREBOARD_FILE_PATH)
        
        # init sprites
        self.snake = Snake(self)
        self.fruit_group = pygame.sprite.GroupSingle()
        
        # init methods
        self._spawn_fruit()

    def run(self) -> None:
        if self.running:
            self.delta_time = self.CLOCK.tick(GameSettings.FPS)
            self.snake.update()
        else:
            self._check_restart()

        self._update_graphics()

    def end_game(self):
        self.running = False
        self.scoreboard.add_score({"name": "kek", "score": self.score})
        self.scoreboard.save()

    def _update_graphics(self) -> None:
        # clear window
        self.WINDOW.fill(GameSettings.BACKGROUND_COLOR)

        # draw
        if self.running:
            self.snake.draw(self.WINDOW)
            self.fruit_group.draw(self.WINDOW)
            self._draw_score()
        else:
            self._draw_game_over()

        # update window
        pygame.display.flip()
    
    def _spawn_fruit(self) -> None:

        found_empty_cell = False
        while not found_empty_cell:
            pos_x_list = [x for x in range(0, self.WINDOW.get_width(), self.cell_size[0])]
            pos_y_list = [y for y in range(0, self.WINDOW.get_height(), self.cell_size[1])]

            pos_x = random.choice(pos_x_list)
            pos_y = random.choice(pos_y_list)

            # test if pos is empty
            test_rect = pygame.rect.Rect((pos_x, pos_y), self.cell_size)
            snake_positions = self.snake.head_group.sprites() + self.snake.tail_group.sprites()
            if test_rect.collidelist(snake_positions) == -1:
                found_empty_cell = True

        self.fruit_group.add(RectSprite(self.cell_size, (pos_x, pos_y), GameSettings.FRUIT_COLOR))
    
    def _draw_score(self) -> None:
        self._draw_center_text(str(self.score), 64)
    
    def _draw_game_over(self) -> None:
        self._draw_center_text("Game Over", 16)
        self._draw_scoreboard()
        self._draw_center_text("Press Enter to restart", GameSettings.WINDOW_WIDTH_AND_HIGHT - 48)
    
    def _draw_scoreboard(self):
        for pos, score in enumerate(self.scoreboard.scores):
            if pos >= 10: break
            text = f"{pos+1}: {score['score']} {score['name']}"
            self._draw_center_text(text, 64+48*pos)

    def _draw_center_text(self, text: str, y_pos: int) -> None:
        text_render = self.FONT.render(text, True, GameSettings.TEXT_COLOR)
        text_width = self.FONT.size(text)[0]
        mid_pos = GameSettings.WINDOW_WIDTH_AND_HIGHT / 2
        pos = (mid_pos - text_width / 2, y_pos)
        self.WINDOW.blit(text_render, pos)

    def _check_restart(self) -> None:
        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[pygame.K_RETURN]:
            pygame.event.post(pygame.event.Event(Events.RESTART))