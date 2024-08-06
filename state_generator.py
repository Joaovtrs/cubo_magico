import csv
import os
from random import choice

import pandas as pd

from cubo import Cubo


def get_resposta(x):
    if len(x) == 2:
        return x[0]
    else:
        return x + "'"


def add_row(df, state, move, layer):
    return df._append(
        pd.DataFrame([[state, move, 0, layer]], columns=df_coluns),
        ignore_index=True,
    )


cubo = Cubo()

df_coluns = ['states', 'move', 'verified', 'layer']

moves = [
    'u',
    "u'",
    'l',
    "l'",
    'f',
    "f'",
    'r',
    "r'",
    'b',
    "b'",
    'd',
    "d'",
]

filepath = os.path.join('.', 'states', 'states.csv')

states = pd.read_csv(filepath)

for _ in range(5000):
    index = states.loc[states['verified'] == 0].first_valid_index()
    state = states.loc[index, 'states']
    layer = states.loc[index, 'layer']

    for move in moves:
        cubo.set_state(state)
        cubo.rotate(move)
        cube_state = cubo.state()

        if cube_state not in states.loc[:, 'states'].values:
            states = add_row(states, cube_state, move, layer + 1)

    states.loc[index, 'verified'] = 1

states.to_csv(filepath, index=False)
