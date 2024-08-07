import os

import numpy as np
import pygame
from pygame.locals import *
from tensorflow.keras.models import load_model

from cubo import Cubo


def draw_cubo():
    for i, r in enumerate(cubo.face_up.blocos):
        for j, c in enumerate(r):
            pygame.draw.rect(
                screen, colors[c], (300 + 100 * j, 000 + 100 * i, 100, 100)
            )
    for i, r in enumerate(cubo.face_left.blocos):
        for j, c in enumerate(r):
            pygame.draw.rect(
                screen, colors[c], (000 + 100 * j, 300 + 100 * i, 100, 100)
            )
    for i, r in enumerate(cubo.face_front.blocos):
        for j, c in enumerate(r):
            pygame.draw.rect(
                screen, colors[c], (300 + 100 * j, 300 + 100 * i, 100, 100)
            )
    for i, r in enumerate(cubo.face_right.blocos):
        for j, c in enumerate(r):
            pygame.draw.rect(
                screen, colors[c], (600 + 100 * j, 300 + 100 * i, 100, 100)
            )
    for i, r in enumerate(cubo.face_back.blocos):
        for j, c in enumerate(r):
            pygame.draw.rect(
                screen, colors[c], (900 + 100 * j, 300 + 100 * i, 100, 100)
            )
    for i, r in enumerate(cubo.face_down.blocos):
        for j, c in enumerate(r):
            pygame.draw.rect(
                screen, colors[c], (300 + 100 * j, 600 + 100 * i, 100, 100)
            )

    for i in range(11):
        pygame.draw.line(
            screen,
            (0, 0, 0),
            (100 + i * 100, 0),
            (100 + i * 100, configs['window_height']),
        )
    for i in range(8):
        pygame.draw.line(
            screen,
            (0, 0, 0),
            (0, 100 + i * 100),
            (configs['window_length'], 100 + i * 100),
        )


def key_event(e):
    global is_model_predicting
    match e.key:
        case pygame.locals.K_q:
            cubo.rotate_up(False)
        case pygame.locals.K_a:
            cubo.rotate_up(True)
        case pygame.locals.K_w:
            cubo.rotate_left(False)
        case pygame.locals.K_s:
            cubo.rotate_left(True)
        case pygame.locals.K_e:
            cubo.rotate_front(False)
        case pygame.locals.K_d:
            cubo.rotate_front(True)
        case pygame.locals.K_r:
            cubo.rotate_right(False)
        case pygame.locals.K_f:
            cubo.rotate_right(True)
        case pygame.locals.K_t:
            cubo.rotate_back(False)
        case pygame.locals.K_g:
            cubo.rotate_back(True)
        case pygame.locals.K_y:
            cubo.rotate_down(False)
        case pygame.locals.K_h:
            cubo.rotate_down(True)
        case pygame.locals.K_z:
            print(cubo.is_assembled())
        case pygame.locals.K_x:
            is_model_predicting = True
        case pygame.locals.K_c:
            is_model_predicting = False
        case pygame.locals.K_SPACE:
            cubo.reset()


def get_one_hot_inputs():
    resp = []
    for s in cubo.state():
        resp += matrix_side[s]

    return np.array([resp])


def model_move():
    move = movimentos[
        np.random.choice(
            np.arange(12), p=model.predict(get_one_hot_inputs(), verbose=0)[0]
        )
    ]
    cubo.rotate(move)


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

matrix_side = {
    'u': [1, 0, 0, 0, 0, 0],
    'l': [0, 1, 0, 0, 0, 0],
    'f': [0, 0, 1, 0, 0, 0],
    'r': [0, 0, 0, 1, 0, 0],
    'b': [0, 0, 0, 0, 1, 0],
    'd': [0, 0, 0, 0, 0, 1],
}
movimentos = ['u', "u'", 'l', "l'", 'f', "f'", 'r', "r'", 'b', "b'", 'd', "d'"]

model_path = os.path.join('.', 'redes', 'model_256_64_12_elu_nadam_10.keras')

clock = pygame.time.Clock()
pygame.init()

screen = pygame.display.set_mode(
    (configs['window_length'], configs['window_height'])
)
pygame.display.set_caption('Cubo')

cubo = Cubo()

model = load_model(model_path)
is_model_predicting = False
move_count = 0

while configs['playing']:
    clock.tick(configs['tick'])

    for event in pygame.event.get():
        if event.type == QUIT:
            configs['playing'] = False
        if event.type == KEYDOWN:
            key_event(event)

    if is_model_predicting:
        model_move()
        move_count += 1
        if cubo.is_assembled():
            print(f'moves: {move_count}')
            is_model_predicting = False
            move_count = 0

    draw_cubo()

    pygame.display.update()

pygame.quit()
exit()
