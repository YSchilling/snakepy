import pygame
from game import Game
from events import Events

def check_keys_pressed_name_screen(scoreboard, event):
    valid_keys = [
            pygame.K_0,
            pygame.K_1,
            pygame.K_2,
            pygame.K_3,
            pygame.K_4,
            pygame.K_5,
            pygame.K_6,
            pygame.K_7,
            pygame.K_8,
            pygame.K_9,
            pygame.K_a,
            pygame.K_b,
            pygame.K_c,
            pygame.K_d,
            pygame.K_e,
            pygame.K_f,
            pygame.K_g,
            pygame.K_h,
            pygame.K_i,
            pygame.K_j,
            pygame.K_k,
            pygame.K_l,
            pygame.K_m,
            pygame.K_n,
            pygame.K_o,
            pygame.K_p,
            pygame.K_q,
            pygame.K_r,
            pygame.K_s,
            pygame.K_t,
            pygame.K_u,
            pygame.K_v,
            pygame.K_w,
            pygame.K_x,
            pygame.K_y,
            pygame.K_z,
        ]

    if event.key == pygame.K_BACKSPACE:
        if len(scoreboard.new_name) != 0:
            scoreboard.new_name.pop()
    elif event.key == pygame.K_RETURN:
        scoreboard.add_score({"name": "".join(scoreboard.new_name), "score": scoreboard.game.score})
        scoreboard.save()
        scoreboard.is_new_name_finished = True
    else:
        if event.key in valid_keys:
            scoreboard.new_name.append(pygame.key.name(event.key))

def main() -> None:
    # init
    pygame.init()
    game = Game()

    # game loop
    run = True
    while run:

        # event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == Events.RESTART:
                game = Game()
            elif event.type == pygame.KEYDOWN and not game.running and not game.scoreboard.is_new_name_finished:
                check_keys_pressed_name_screen(game.scoreboard, event)

        # game tick
        game.run()
    
    pygame.quit()

if __name__ == "__main__": main()