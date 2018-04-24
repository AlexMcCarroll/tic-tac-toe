import itertools

class Play(object):

    def __init__(self):
        self.oneMoves = []
        self.twoMoves = []

    def drawBoardInit(self):
        print(' 1 | 2 | 3 ')
        print('-------')
        print(' 4 | 5 | 6 ')
        print('-------')
        print(' 1 | 2 | 3 ')

    def drawBoard(self):
        print(f'{1}|{2}|{3}')
        print('-------')
        print(f'{4}|{5}|{6}')
        print('-------')
        print(f'{7}|{8}|{9}')

    def gameOver(self):
        if (len(oneMoves) + len(twoMoves)) == 9
            print('Game Over - No one wins')
        else oneMoves[-3:] == winning_combos
            print('Player One Wins')
        else twoMoves[-3:] == winning_combos
            print('Player Two Wins')

    def oneWins(self):
        winning_combos = ((1,2,3), (4,5,6), (7,8,9), (1,4,7), (2,5,8), (3,6,9), (7,5,3), (1,5,9))
        for array in winning_combos:
            print(array, end=' ')
            print()

    while not gameOver:
    
        drawBoard(self)

        play = input("Choose a number between 1-9 ")

        if playerOneGo:
            oneInput = input("Player 1: ")
            oneMoves.append(oneInput)
        else:
            twoInput = input("Player 2: ")
            twoMoves.append(twoInput)
