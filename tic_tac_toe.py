
x = "X"
o = "O"
_ = "_"

emptyBoard = [_, _, _, _, _, _, _, _, _]


def inverse(symbol):
    if(symbol == o):
        return x
    return o


class TicTacToe:

    turn = None
    board = None

    def __init__(self, turn=o, board=emptyBoard):
        self.turn = turn
        self.board = board

    def printBoard(self):
        print(self.board[0], "|", self.board[1], "|", self.board[2],
              "    0 | 1 | 2")
        print(self.board[3], "|", self.board[4], "|", self.board[5],
              "    3 | 4 | 5")
        print(self.board[6], "|", self.board[7], "|", self.board[8],
              "    6 | 7 | 8")
        print()
        if (self.winner()):
            print("Winner is:", self.winner())
            print()
        if (self.draw()):
            print("It's a draw")
            print()

    def mark(self, position):
        if(position not in range(9)):
            print("Invalid position")
            print()
            return
        if(self.board[position] != _):
            print("Tile occupied")
            print()
            return
        self.board[position] = self.turn
        self.turn = inverse(self.turn)
        return True

    def markedEqual(self, pos1, pos2, pos3, symbol):
        return self.board[pos1] == symbol and self.board[pos1] == self.board[pos2] and self.board[pos2] == self.board[pos3]

    def winnerIs(self, symbol):
        horizontal = self.markedEqual(0, 1, 2, symbol) or self.markedEqual(
            3, 4, 5, symbol) or self.markedEqual(6, 7, 8, symbol)
        vertical = self.markedEqual(0, 3, 6, symbol) or self.markedEqual(
            1, 4, 7, symbol) or self.markedEqual(2, 5, 8, symbol)
        diagonal = self.markedEqual(
            0, 4, 8, symbol) or self.markedEqual(2, 4, 6, symbol)
        return horizontal or vertical or diagonal

    def draw(self):
        for tile in self.board:
            if (tile == _):
                return False
        return self.winner() == None

    def winner(self):
        if (self.winnerIs(o)):
            return o
        if (self.winnerIs(x)):
            return x
        return None

    def gameEnded(self):
        return self.winner() != None or self.draw()

    def emptyTiles(self):
        return list(filter(lambda tile: self.board[tile] == _, range(9)))

    def resultingGame(self, tile):
        newGame = TicTacToe(self.turn, self.board.copy())
        newGame.mark(tile)
        return newGame
