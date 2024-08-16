class board:
    def __init__(self):
        self.board = [["", "", ""], ["", "", ""], ["", "", ""]]
    def isMarked(self, x, y):
        return self.board[x][y] != ""