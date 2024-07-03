from random import choice

from cubo import Cubo


def get_resposta(x):
    if len(x) == 2:
        return x[0]
    else:
        return x + "'"


cubo = Cubo()

movimentos = [
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

for i in range(1_000):
    cubo.reset()
    m = choice([10, 10, 10, 20, 20, 20, 30, 30, 30, 50, 100])
    print(f'Cubo {i + 1} com {m} movimentos')

    for _ in range(m):
        c = choice(movimentos)
        cubo.rotate(c)
        with open('states.txt', 'a') as file:
            file.write(cubo.state() + ',' + get_resposta(c) + '\n')
