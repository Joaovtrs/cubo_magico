import pickle
from pprint import pprint
from random import choice

import numpy as np

from cubo import Cubo
from pynapse.brain import Camada, RedeNeural
from pynapse.brain.funcs_ativacao import FuncSoftmax, FuncTanh
from pynapse.brain.funcs_custo import FuncNegLogLikelihood


def generate_states(n_moves):
    cubo.reset()
    data = []

    for _ in range(n_moves):
        move = choice(list(matrix_moves.keys()))
        cubo.rotate(move)

        state = []
        for side in cubo.state():
            state += matrix_side[side]
            # state.append(side)

        data.append([state, matrix_reset[move]])

    data = remove_invalid(data)
    x, y = [], []

    for x_, y_ in data:
        y.append(matrix_moves[y_])
        x.append(x_)

    return np.array(x), np.array(y)


def remove_invalid(data):
    change = False

    for i in range(len(data) - 1):
        if data[i][1] == matrix_reset[data[i + 1][1]]:
            change = True
            data.pop(i + 1)
            data.pop(i)
            break

    for i in range(len(data) - 2):
        if data[i][1] == data[i + 1][1] == data[i + 2][1]:
            change = True
            data[i + 2][1] = matrix_reset[data[i + 2][1]]
            data.pop(i + 1)
            data.pop(i)
            break

    if change:
        data = remove_invalid(data)

    return data


matrix_moves = {
    'u': [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "u'": [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'l': [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "l'": [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    'f': [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    "f'": [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    'r': [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    "r'": [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    'b': [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    "b'": [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    'd': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    "d'": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
}

matrix_side = {
    'u': [1, 0, 0, 0, 0, 0],
    'l': [0, 1, 0, 0, 0, 0],
    'f': [0, 0, 1, 0, 0, 0],
    'r': [0, 0, 0, 1, 0, 0],
    'b': [0, 0, 0, 0, 1, 0],
    'd': [0, 0, 0, 0, 0, 1],
}

matrix_reset = {
    'u': "u'",
    "u'": 'u',
    'l': "l'",
    "l'": 'l',
    'f': "f'",
    "f'": 'f',
    'r': "r'",
    "r'": 'r',
    'b': "b'",
    "b'": 'b',
    'd': "d'",
    "d'": 'd',
}

cubo = Cubo()

if __name__ == '__main__':
    nn = RedeNeural(
        [
            Camada(288, 256, FuncTanh()),
            Camada(256, 64, FuncTanh()),
            Camada(64, 12, FuncSoftmax()),
        ]
    )

    for i in range(10_001):
        x, y = generate_states(50)

        custo = nn.backprop(
            x, y, FuncNegLogLikelihood(), 0.01, 0.1
        )

        if i % 100 == 0:
            print(f'{i:_}: {custo}')
            if i % 1_000 == 0:
                with open(f'redes/rede_{i:_}.pck', 'wb') as arquivo:
                    pickle.dump(nn, arquivo)
