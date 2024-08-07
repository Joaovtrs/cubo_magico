import numpy as np


class Face:
    def __init__(self, cor):
        self.blocos = np.array(
            [[cor, cor, cor], [cor, cor, cor], [cor, cor, cor]]
        )

    def rotate(self, reverse):
        p1 = self.blocos[0, 0]
        p2 = self.blocos[0, 1]
        p3 = self.blocos[0, 2]
        p4 = self.blocos[1, 2]
        p5 = self.blocos[2, 2]
        p6 = self.blocos[2, 1]
        p7 = self.blocos[2, 0]
        p8 = self.blocos[1, 0]

        if reverse:
            self.blocos[0, 0] = p3
            self.blocos[0, 1] = p4
            self.blocos[0, 2] = p5
            self.blocos[1, 2] = p6
            self.blocos[2, 2] = p7
            self.blocos[2, 1] = p8
            self.blocos[2, 0] = p1
            self.blocos[1, 0] = p2
        else:
            self.blocos[0, 0] = p7
            self.blocos[0, 1] = p8
            self.blocos[0, 2] = p1
            self.blocos[1, 2] = p2
            self.blocos[2, 2] = p3
            self.blocos[2, 1] = p4
            self.blocos[2, 0] = p5
            self.blocos[1, 0] = p6

    def get_up(self):
        return self.blocos[0].copy()

    def get_left(self):
        return self.blocos[:, 0].copy()

    def get_right(self):
        return self.blocos[:, 2].copy()

    def get_down(self):
        return self.blocos[2].copy()

    def set_up(self, colors):
        self.blocos[0] = colors

    def set_left(self, colors):
        self.blocos[:, 0] = colors

    def set_right(self, colors):
        self.blocos[:, 2] = colors

    def set_down(self, colors):
        self.blocos[2] = colors

    def reset(self):
        self.blocos[:, :] = self.blocos[1, 1]

    def state(self):
        return (
            self.blocos[0, 0]
            + self.blocos[0, 1]
            + self.blocos[0, 2]
            + self.blocos[1, 0]
            + self.blocos[1, 2]
            + self.blocos[2, 0]
            + self.blocos[2, 1]
            + self.blocos[2, 2]
        )

    def set_state(self, state):
        self.blocos[0, 0] = state[0]
        self.blocos[0, 1] = state[1]
        self.blocos[0, 2] = state[2]
        self.blocos[1, 0] = state[3]
        self.blocos[1, 2] = state[4]
        self.blocos[2, 0] = state[5]
        self.blocos[2, 1] = state[6]
        self.blocos[2, 2] = state[7]

    def is_assembled(self):
        return (
            self.blocos[0][0] == self.blocos[1, 1]
            and self.blocos[0][1] == self.blocos[1, 1]
            and self.blocos[0][2] == self.blocos[1, 1]
            and self.blocos[1][0] == self.blocos[1, 1]
            and self.blocos[1][2] == self.blocos[1, 1]
            and self.blocos[2][0] == self.blocos[1, 1]
            and self.blocos[2][1] == self.blocos[1, 1]
            and self.blocos[2][2] == self.blocos[1, 1]
        )
