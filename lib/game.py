from . import player, board
class game:
    def __init__ (self):
        var = input("Please enter your char of choice - ")
        var2 = input("Please enter your char of choice - ")
        self.player1 = player.player(var, True)
        self.player2 = player.player(var2, False)
        self.board = board.board()
    def isWinner(self):
        if self.board.board[0][0] == self.board.board[0][1] and self.board.board[0][1] == self.board.board[0][2] and self.board.board[0][2] != '':
            return True
        elif self.board.board[1][0] == self.board.board[1][1] and self.board.board[1][1] == self.board.board[1][2] and self.board.board[1][1] != '':
            return True
        elif self.board.board[2][0] == self.board.board[2][1] and self.board.board[2][1] == self.board.board[2][2] and self.board.board[2][1] != '':
            return True
        elif self.board.board[0][0] == self.board.board[1][0] and self.board.board[2][0] == self.board.board[1][0] and self.board.board[2][0] != '':
            return True
        elif self.board.board[0][1] == self.board.board[1][1] and self.board.board[2][1] == self.board.board[1][1] and self.board.board[1][1] != '':
            return True
        elif self.board.board[0][2] == self.board.board[1][2] and self.board.board[2][2] == self.board.board[1][2] and self.board.board[1][2] != '':
            return True
        elif self.board.board[0][2] == self.board.board[1][1] and self.board.board[2][0] == self.board.board[1][1] and self.board.board[1][1] != '':
            return True
        elif self.board.board[2][0] == self.board.board[1][1] and self.board.board[0][2] == self.board.board[1][1] and self.board.board[1][1] != '':
            return True
        else:
            return False
    def handleTurn (self, x, y):
        while self.board.isMarked(x, y):
            currentSpot = input("place another cooridinate - ")
            newSpot = currentSpot.split(' ')
            (x, y) = (int(newSpot[0]), int(newSpot[1]))
        if self.player1.isTurn:
            self.board.board[x][y] = self.player1.char
            (self.player1.isTurn, self.player2.isTurn) = (False, True)
        else:
            self.board.board[x][y] = self.player2.char
            (self.player1.isTurn, self.player2.isTurn) = (True, False)
        if self.isWinner():
            return True
        else:
            return False