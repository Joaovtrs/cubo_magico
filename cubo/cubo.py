from .face import Face


class Cubo:
    def __init__(self):
        self.face_up = Face('u')
        self.face_left = Face('l')
        self.face_front = Face('f')
        self.face_right = Face('r')
        self.face_back = Face('b')
        self.face_down = Face('d')

    def rotate(self, lado):
        match lado:
            case "u":
                self.rotate_up(False)
            case "u'":
                self.rotate_up(True)
            case "l":
                self.rotate_left(False)
            case "l'":
                self.rotate_left(True)
            case "f":
                self.rotate_front(False)
            case "f'":
                self.rotate_front(True)
            case "r":
                self.rotate_right(False)
            case "r'":
                self.rotate_right(True)
            case "b":
                self.rotate_back(False)
            case "b'":
                self.rotate_back(True)
            case "d":
                self.rotate_down(False)
            case "d'":
                self.rotate_down(True)

    def rotate_up(self, reverse):
        self.face_up.rotate(reverse)

        left = self.face_left.get_up()
        front = self.face_front.get_up()
        right = self.face_right.get_up()
        back = self.face_back.get_up()

        if reverse:
            self.face_left.set_up(back)
            self.face_front.set_up(left)
            self.face_right.set_up(front)
            self.face_back.set_up(right)
        else:
            self.face_left.set_up(front)
            self.face_front.set_up(right)
            self.face_right.set_up(back)
            self.face_back.set_up(left)

    def rotate_left(self, reverse):
        self.face_left.rotate(reverse)

        up = self.face_up.get_left()
        front = self.face_front.get_left()
        down = self.face_down.get_left()
        back = self.face_back.get_right()

        if reverse:
            self.face_up.set_left(front)
            self.face_front.set_left(down)
            self.face_down.set_left(back[::-1])
            self.face_back.set_right(up[::-1])
        else:
            self.face_up.set_left(back[::-1])
            self.face_front.set_left(up)
            self.face_down.set_left(front)
            self.face_back.set_right(down[::-1])

    def rotate_front(self, reverse):
        self.face_front.rotate(reverse)

        left = self.face_left.get_right()
        up = self.face_up.get_down()
        right = self.face_right.get_left()
        down = self.face_down.get_up()

        if reverse:
            self.face_left.set_right(up[::-1])
            self.face_up.set_down(right)
            self.face_right.set_left(down[::-1])
            self.face_down.set_up(left)
        else:
            self.face_left.set_right(down)
            self.face_up.set_down(left[::-1])
            self.face_right.set_left(up)
            self.face_down.set_up(right[::-1])

    def rotate_right(self, reverse):
        self.face_right.rotate(reverse)

        up = self.face_up.get_right()
        back = self.face_back.get_left()
        down = self.face_down.get_right()
        front = self.face_front.get_right()

        if reverse:
            self.face_up.set_right(back[::-1])
            self.face_back.set_left(down[::-1])
            self.face_down.set_right(front)
            self.face_front.set_right(up)
        else:
            self.face_up.set_right(front)
            self.face_back.set_left(up[::-1])
            self.face_down.set_right(back[::-1])
            self.face_front.set_right(down)

    def rotate_back(self, reverse):
        self.face_back.rotate(reverse)

        up = self.face_up.get_up()
        right = self.face_right.get_right()
        down = self.face_down.get_down()
        left = self.face_left.get_left()

        if reverse:
            self.face_up.set_up(left[::-1])
            self.face_right.set_right(up)
            self.face_down.set_down(right[::-1])
            self.face_left.set_left(down)
        else:
            self.face_up.set_up(right)
            self.face_right.set_right(down[::-1])
            self.face_down.set_down(left)
            self.face_left.set_left(up[::-1])

    def rotate_down(self, reverse):
        self.face_down.rotate(reverse)

        front = self.face_front.get_down()
        right = self.face_right.get_down()
        back = self.face_back.get_down()
        left = self.face_left.get_down()

        if reverse:
            self.face_front.set_down(right)
            self.face_right.set_down(back)
            self.face_back.set_down(left)
            self.face_left.set_down(front)
        else:
            self.face_front.set_down(left)
            self.face_right.set_down(front)
            self.face_back.set_down(right)
            self.face_left.set_down(back)

    def reset(self):
        self.face_up.reset()
        self.face_left.reset()
        self.face_front.reset()
        self.face_right.reset()
        self.face_back.reset()
        self.face_down.reset()
