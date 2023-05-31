import pygame
from game import Game

def main():
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
    
    pygame.quit()

if __name__ == "__main__": main()