from lib import board, game, player
def startGame ():
    isFinished = False
    newGame = game.game()
    while isFinished == False:
        coordinates = input("enter coordinates - ")
        newList = coordinates.split(" ")
        isFinished = newGame.handleTurn(int(newList[0]), int(newList[1]))
        print(str(newGame.board.board[0]) + '\n' + str(newGame.board.board[1]) + '\n' + str(newGame.board.board[2]))
    if newGame.player1.isTurn:
        print("Player 2 has won")
    else:
        print("Player 1 has won")
startGame()