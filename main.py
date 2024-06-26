import pygame
from pygame.locals import *

from cubo import Cubo


def draw_cubo():
    for i, r in enumerate(cubo.face_up.blocos):
        for j, c in enumerate(r):
            pygame.draw.rect(
                screen,
                colors[c],
                (300 + 100 * j, 000 + 100 * i, 100, 100)
            )
    for i, r in enumerate(cubo.face_left.blocos):
        for j, c in enumerate(r):
            pygame.draw.rect(
                screen,
                colors[c],
                (000 + 100 * j, 300 + 100 * i, 100, 100)
            )
    for i, r in enumerate(cubo.face_front.blocos):
        for j, c in enumerate(r):
            pygame.draw.rect(
                screen,
                colors[c],
                (300 + 100 * j, 300 + 100 * i, 100, 100)
            )
    for i, r in enumerate(cubo.face_right.blocos):
        for j, c in enumerate(r):
            pygame.draw.rect(
                screen,
                colors[c],
                (600 + 100 * j, 300 + 100 * i, 100, 100)
            )
    for i, r in enumerate(cubo.face_back.blocos):
        for j, c in enumerate(r):
            pygame.draw.rect(
                screen,
                colors[c],
                (900 + 100 * j, 300 + 100 * i, 100, 100)
            )
    for i, r in enumerate(cubo.face_down.blocos):
        for j, c in enumerate(r):
            pygame.draw.rect(
                screen,
                colors[c],
                (300 + 100 * j, 600 + 100 * i, 100, 100)
            )

    for i in range(11):
        pygame.draw.line(
            screen,
            (0, 0, 0),
            (100 + i * 100, 0),
            (100 + i * 100, configs['window_height'])
        )
    for i in range(8):
        pygame.draw.line(
            screen,
            (0, 0, 0),
            (0, 100 + i * 100),
            (configs['window_length'], 100 + i * 100)
        )


def key_event(e):
    if e.key == K_q:
        cubo.rotate_up(False)
    if e.key == K_a:
        cubo.rotate_up(True)
    if e.key == K_w:
        cubo.rotate_left(False)
    if e.key == K_s:
        cubo.rotate_left(True)
    if e.key == K_e:
        cubo.rotate_front(False)
    if e.key == K_d:
        cubo.rotate_front(True)
    if e.key == K_r:
        cubo.rotate_right(False)
    if e.key == K_f:
        cubo.rotate_right(True)
    if e.key == K_t:
        cubo.rotate_back(False)
    if e.key == K_g:
        cubo.rotate_back(True)
    if e.key == K_y:
        cubo.rotate_down(False)
    if e.key == K_h:
        cubo.rotate_down(True)
    if e.key == K_SPACE:
        cubo.reset()


configs = {
    'playing': True,
    'tick': 60,
    'window_height': 900,
    'window_length': 1200,
}
colors = {
    'u': (230, 230, 230),
    'l': (230, 0, 0),
    'f': (0, 230, 0),
    'r': (0, 0, 230),
    'b': (230, 230, 0),
    'd': (230, 130, 0),
}

clock = pygame.time.Clock()
pygame.init()

screen = pygame.display.set_mode(
    (configs['window_length'], configs['window_height'])
)
pygame.display.set_caption('Name here')

cubo = Cubo()

while configs['playing']:
    clock.tick(configs['tick'])

    for event in pygame.event.get():
        if event.type == QUIT:
            configs['playing'] = False
        if event.type == KEYDOWN:
            key_event(event)

    draw_cubo()

    pygame.display.update()

pygame.quit()
exit()
