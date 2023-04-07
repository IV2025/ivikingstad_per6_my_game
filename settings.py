WIDTH = 800
HEIGHT = 600
PLAYER_ACC = 2
PLAYER_FRICTION = -0.3
PLAYER_JUMP = 20
PLAYER_GRAV = 1
MOB_ACC = 2
MOB_FRICTION = -0.3
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
RED = (255,50,50)
PURPLE = (138,43,226)
DARKGREY = (74,74,74)
AQUAMARINE = (72,209,204)
FPS = 60
RUNNING = True
SCORE = 0
PAUSED = False

# Starting platforms
PLATFORM_LIST = [(0, HEIGHT - 40, WIDTH, 40, (DARKGREY), "normal"),
                 (WIDTH / 2 - 10, HEIGHT * 3 / 4, 200, 20, (PURPLE), "bouncey"),
                 (125, HEIGHT - 500, 100, 25, (PURPLE), "disappearing "),
                 (500, 200, 250, 40, (PURPLE), "normal"),
                 (250, 500, 50, 20, (PURPLE), "normal"),
                 (200, 450, 50, 20, (PURPLE), "normal"),
                 (150, 400, 50, 20, (PURPLE), "normal"),
                 (100, 350, 50, 20, (PURPLE), "normal"),
                 (50, 300, 50, 20, (PURPLE), "normal")]