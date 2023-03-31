WIDTH = 800
HEIGHT = 600
PLAYER_ACC = 2
PLAYER_FRICTION = -0.3
PLAYER_JUMP = 20
PLAYER_GRAV = 0.8
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
                 (WIDTH / 2 - 10, HEIGHT * 3 / 4, 100, 20, (PURPLE), "bouncey"),
                 (125, HEIGHT - 350, 100, 5, (PURPLE), "disappearing "),
                 (500, 200, 100, 40, (PURPLE), "normal"),
                 (175, 500, 50, 20, (PURPLE), "normal")]