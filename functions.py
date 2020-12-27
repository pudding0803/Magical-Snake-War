import pygame
import random

from constants import *
from classes import *


def draw_square(color, x, y, width):
    pygame.draw.rect(SCREEN, color, pygame.Rect(x, y, width, width))


def spawn_berry(berry_idx, berry_ls, a_body_pos_ls, b_body_pos_ls, init):
    rate = random.randint(1, 100)
    special_berry = (rate % 3 == 0)
    super_berry = (rate % 7 == 0)
    for idx in range(BERRY_NUM):
        if idx != berry_idx and berry_ls[idx].score < 5 and not init:
            berry_ls[idx].remote += 1
        if berry_ls[idx].remote == 6:
            berry_ls[idx].score += 2
            berry_ls[idx].remote = 0
    berry = Berry(
        berry_idx,
        Coord(
            random.randint(0, RAND_X) * 16,
            random.randint(0, RAND_Y) * 16
        ),
        True,
        1 + special_berry * 2 + super_berry * 2
    )
    while True:
        overlap = False
        if berry.coord in a_body_pos_ls or berry.coord in b_body_pos_ls:
            berry.coord = (
                random.randint(0, RAND_X) * 16,
                random.randint(0, RAND_Y) * 16
            )
            overlap = True
            break
        for idx in range(BERRY_NUM):
            if berry.coord == berry_ls[idx].coord and berry_idx != berry_ls[idx].coord:
                berry.coord = (
                random.randint(0, RAND_X) * 16,
                random.randint(0, RAND_Y) * 16
                )
                overlap = True
                break
        if not overlap:
            break
    berry_ls[berry_idx] = berry
    return berry_ls


def gameover_execute(a_alive, b_alive):
    gameover = False
    if not a_alive and not b_alive:
        content = 'Both Die...'
        color = RED
        gameover = True
    elif not a_alive:
        content = 'Snake B Win!'
        color = YELLOW
        gameover = True
    elif not b_alive:
        content = 'Snake A Win!'
        color = YELLOW
        gameover = True
    if gameover:
        text = GAMEOVER_FONT.render(content, True, color)
        rect = text.get_rect()
        rect.center = SCREEN_CENTER
        SCREEN.blit(text, rect)
        pygame.display.flip()
    return gameover
