class Board:
    def __init__(self):
        self.pieces = []
        self.pieces.append(Piece('black', Square(1, 'a')))
        self.pieces.append(Piece('white', Square(8, 'h')))


class Square:
    def __init__(self, num, char):
        self.num = num
        self.char = char

    def toa(self):

    def movedforward(self, color):
        if color == 'white':
            self.num += 1
        else:
            self.num -= 1

    def movedside(self, color, side):
        if color == 'white' and side == 'left' or color == 'black' and side == 'right':
            self.toa()
        else:
            self.tob()

class Piece:
    def __init__(self, color, square:Square):
        self.color = color
        self.square = square
        self.ingame = True

class Pawn(Piece):
    def __init__(self, color, square):
        super().__init__(color, square)
        self.moved = False

    def movenormal(self):
        self.square.movedforward(self.color)

    def movedouble(self):
        self.square.movedforward(self.color)
        self.square.movedforward(self.color)
    def hit(self, side):
        self.square.movedforward(self.color)
        self.square.movedside(self.color, side)