#yeet TicTacToe
import os
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
def printBoard():
    print("+-----------------+")
    print("|  " + str(board[0]) + "  |  " + str(board[1]) + "  |  " + str(board[2]) + "  |")
    print("+-----+-----+-----+")
    print("|  " + str(board[3]) + "  |  " + str(board[4]) + "  |  " + str(board[5]) + "  |")
    print("+-----+-----+-----+")
    print("|  " + str(board[6]) + "  |  " + str(board[7]) + "  |  " + str(board[8]) + "  |")
    print("+-----------------+")
def testCase(player):
    if board[0] == player and board[1] == player and board[2] == player:
        return 0;
    elif board[3] == player and board[4] == player and board[5] == player:
        return 0;
    elif board[6] == player and board[7] == player and board[8] == player:
        return 0;
    elif board[0] == player and board[4] == player and board[8] == player:
        return 0;
    elif board[2] == player and board[4] == player and board[6] == player:
        return 0;
    elif board[0] == player and board[3] == player and board[6] == player:
        return 0;
    elif board[1] == player and board[4] == player and board[7] == player:
        return 0;
    elif board[2] == player and board[5] == player and board[8] == player:
        return 0;
    else:
        return 1;

def turn(player, name):
    cls()
    print("It is "+ name +"'s turn")
    printBoard()
    loc = int(input("Choose a location to play: "))
    while loc < 0 or loc > 8:
        loc = int(input("Choose a location to play: "))
    if player == 1:
        type = "X"
    else:
        type = "O"
    board[loc] = type
    if testCase(type) == 0:
        return 1
    else:
        return 0
def endGame(player):
    if player == 1:
        type = "X"
    else:
        type = "O"
    if testCase(type) == 0:
        return 1
    else:
        return 0
board = ["0","1","2","3","4","5","6","7","8"]
print("Tic Tac Toe!")
print("")
print("Player 1's name?")
p1 = input()
print("You are 'X'")
print("Player 2's name?")
p2 = input()
print("You are 'O'")
current = 1
name = p1
gameOver = 1
turns = 0
while gameOver == 1:
    turn(current, name)
    if endGame(current) == 1:
        break
    if current == 1:
        current = 2
    else:
        current = 1
    if name == p1:
        name = p2
    else:
        name = p1
    turns = turns +1
    if turns == 9:
        break
if turns ==9:
    print("Tie Game!")
else:
    if current == 1:
        print(p1 + " Won!!")
    else:
        print(p2 + " Won!!")
