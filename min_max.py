from tic_tac_toe import o, TicTacToe, x
import sys

minimum = o
maximum = x

user = minimum
comp = maximum


def score(state):
    if(state.winnerIs(comp)):
        return 10
    if(state.winnerIs(user)):
        return -10
    if(state.draw()):
        return 0
    raise "Game didn't end"


def utilityValue(state):
    if(state.gameEnded()):
        return score(state)
    return utilityValue(state.resultingGame(decision(state)))


def decision(gameState):
    possibleTiles = gameState.emptyTiles()
    if(gameState.turn == maximum):
        return max(possibleTiles, default=None, key=lambda tile: utilityValue(gameState.resultingGame(tile)))
    if(gameState.turn == minimum):
        return min(possibleTiles, default=None, key=lambda tile: utilityValue(gameState.resultingGame(tile)))


print()
print("User: ", user)
print("Comp: ", comp)
print()
print("Comp as MAX")
print()

fisrtPlayer = comp if len(sys.argv) >= 2 and sys.argv[1] == "-c" else user

game = TicTacToe(fisrtPlayer)

game.printBoard()
print("======================")
print()

while(not game.gameEnded()):

    while game.turn == user:
        tile = input("User move: ")
        if(tile.isdigit() and game.mark(int(tile))):
            game.printBoard()
            print("=====================")
            print()

    if(not game.gameEnded()):
        warn = "(may take a while)" if len(game.emptyTiles()) >= 8 else ""
        print("Computer is deciding it's move...", warn)
        tile = decision(game)
        print("Computer move:", tile)
        print()
        game.mark(tile)
        game.printBoard()
        print("=====================")
        print()
