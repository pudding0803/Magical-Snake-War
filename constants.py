import pygame

VERSION = '1.0.1 beta'

DISPLAY_WIDTH = 1136
DISPLAY_HEIGHT = 640

SCREEN = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
SCREEN_CENTER = (DISPLAY_WIDTH // 2, DISPLAY_HEIGHT // 2)
CLOCK = pygame.time.Clock()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
MAGENTA = (255, 0, 255)

BERRY_NUM = 3
SUPER_COLOR_LS = [YELLOW, CYAN, MAGENTA]

UP = 1
DOWN = -1
LEFT = 2
RIGHT = -2

SNAKE_SIZE = 16

RAND_X = 70
RAND_Y = 39

pygame.init()
pygame.display.set_caption("Magical Snake War ver" + VERSION)

SCORE_FONT = pygame.font.SysFont('consolas', 32)
GAMEOVER_FONT = pygame.font.SysFont('consolas', 60)
