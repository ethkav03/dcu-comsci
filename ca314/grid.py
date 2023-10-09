class Piece (object):
    def __init__(self, y, x):
        self.x = x
        self.y = y
        self.north = None
        self.south = None
        self.east = None
        self.west = None

    def setNorth(self, piece):
        self.north = piece

    def setSouth(self, piece):
        self.south = piece

    def setEast(self, piece):
        self.east = piece

    def setWest(self, piece):
        self.west = piece

    def __str__(self):
        return f"{self.y}, {self.x}"

class Board (object):
    def __init__(self):
        self.board = []

        for i in range(5):
            for j in range(5):
                self.board.append(Piece(i, j))

        for i in range(5):
            for j in range(5):
                if i - 1 >= 0:
                    self.board[i][j].setNorth(self.board[i - 1][j])
                if i + 1 < 5:
                    self.board[i][j].setSouth(self.board[i + 1][j])
                if j + 1 >= 0:
                    self.board[i][j].setEast(self.board[i][j + 1])
                if j - 1 < 5:
                    self.board[i][j].setWest(self.board[i][j - 1])
        
    def __str__(self):
        return f"{self.board}"

print(Board())