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

    def rotate_front(self, reverse):
        self.face_front.rotate(reverse)

    def rotate_right(self, reverse):
        self.face_right.rotate(reverse)

    def rotate_back(self, reverse):
        self.face_back.rotate(reverse)

    def rotate_down(self, reverse):
        self.face_down.rotate(reverse)
