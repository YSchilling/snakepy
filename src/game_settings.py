class GameSettings:
    # game
    FPS = 60
    WINDOW_WIDTH_AND_HIGHT = 600
    CELL_AMOUNT = 20 # needs to fit into WINDOW_WIDTH_AND_HIGHT
    SCOREBOARD_FILE_PATH = "scores.txt"

    # snake
    MOVES_PER_SECOND = 1.5
    
    # colors
    BACKGROUND_COLOR = (30, 30, 30)
    SNAKE_HEAD_COLOR = (0, 200, 0)
    SNAKE_TAIL_COLOR = (0, 255, 0)
    FRUIT_COLOR = (153, 153, 255)
    TEXT_COLOR = (255, 255, 255)