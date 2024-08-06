import os

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from tensorflow.keras import layers, models

from cubo import Cubo


def get_one_hot_inputs(state):
    resp = []
    for s in state:
        resp += matrix_side[s]

    return np.array(resp)


def get_one_hot_target(move):
    return np.array(matrix_moves.index(matrix_reset[move]))


matrix_moves = [
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

filepath = os.path.join('.', 'states', 'states.csv')
model_path = os.path.join('.', 'redes')

states = pd.read_csv(filepath)

cubo = Cubo()

X = states.loc[:, 'states'].map(get_one_hot_inputs).values
y = states.loc[:, 'move'].map(get_one_hot_target).values

X = np.stack(X)

del states

X_train_full, X_test, y_train_full, y_test = train_test_split(
    X, y, test_size=0.15, random_state=42
)
X_train, X_valid, y_train, y_valid = train_test_split(
    X_train_full, y_train_full, test_size=0.15, random_state=42
)

model = models.Sequential(
    [
        layers.Input(shape=X_train.shape[1:]),
        layers.Dense(256, activation='elu', kernel_initializer='he_normal'),
        layers.Dense(64, activation='elu', kernel_initializer='he_normal'),
        layers.Dense(12, activation='softmax'),
    ]
)

model.compile(
    loss='sparse_categorical_crossentropy',
    optimizer='nadam',
    metrics=['accuracy'],
)

history = model.fit(
    X_train,
    y_train,
    epochs=10,
    validation_data=(X_valid, y_valid),
)

model.save(os.path.join(model_path, 'model_256_64_12_elu_nadam_10.keras'))
