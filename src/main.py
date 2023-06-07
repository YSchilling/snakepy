import pygame
from game import Game
from events import Events

def main() -> None:
    # init
    pygame.init()
    game = Game()

    # game loop
    run: bool = True
    while run:

        # event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == Events.RESTART:
                game = Game()

        # game tick
        game.run()
    
    pygame.quit()

if __name__ == "__main__": main()