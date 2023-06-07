import pygame
from game import Game

def main() -> none:
    # init
    pygame.init()
    game: Game = Game()

    # game loop
    run: bool = True
    while run:

        # event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # game tick
        game.run()
    
    pygame.quit()

if __name__ == "__main__": main()