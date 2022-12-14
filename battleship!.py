"""
Name: Ellie Hochberg
Date: Dec 16, 2022
Description: Play a game of battleship with the computer
Bugs: No bugs
Plan:
    1)Generate a board for both the player and the computer with four randomly placed ships
    2)Ask the player where they want to shoot
    3)Put a * if they didn't hit a ship and a ! if they did on the computer's board
    4)Computer shoots a random spot
    5)Put a * if they didn't hit a ship and a ! if they did on the player's board
    6)Repeat until there is a winner
"""
import random
from playsound import playsound

def startBoard(board):
    """
    Generate a randomized board with 4 randomly placed ships
    Arguments:
        board: the randomly generated board
    Returns:
        The board with the 4 ships
    """
    i=0
    while i < 4:                       #run loop 4 times
        r = random.randint(0,4)          #random number from 0-4
        c = random.randint(0,4)           #random number from 0-4

        if board[r][c] == "X":                    #if spot already chosen, try again
            continue
        else:
            board[r][c]="X"                    #put an X in that spot
            i+=1

    return board


def printBoard(board):
    """
    Print a board
    Arguments:
        board: the board
    Returns:
        A board
    """

    for r in board:
        for c in r:
            print(c,end = "")
        print()

def changeBoard(board, game):
    """
    Print a board
    Arguments:
        board: the board
        game: whether the game is still going or not
    Returns:
        A game board
    """
    if game == 1:
        doneGame()

    else:
        print('')

        for r in board:
            for c in r:
                print(c,end = " ")
            print()


def playerChoice(compBoard):
    """
    The player's choice of where to shoot
    Arguments:
        compBoard: the computer's board
    Returns:
        A * on the board if there is no ship in that spot
        A ! on the board if there is a ship in that spot
    """

    trying = True
    while trying:
        trying = False
        try:
            r = input("Pick a row")  # row
            c = input("Pick a column")  # column
        except:
            print("Please enter a number")
            trying = True

    if 0>r>4 or 0>c>4:
        print("Choose a valid number")
        playerChoice(compBoard)

    elif (compBoard[r][c] == "X"):                         #if ship in that spot
        compBoard[r][c] = "!"
        print("You hit a ship!")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\explosion.wav')

    elif (compBoard[r][c] == "*") or (compBoard[r][c] == "!"):                  #if spot already taken
        print("Spot already chosen. Choose again")
        playerChoice(compBoard)

    else:
        compBoard[r][c] = "*"                        #put a * where the player chose

    return compBoard

def computerChoice(playerBoard):
    """
    Randomize the computer's choice of where to shoot
    Arguments:
        playerBoard: the player's board
    Returns:
        A * on the board if there is no ship in that spot
        A ! on the board if there is a ship in that spot
        """

    r = random.randint(0,4)                         #random r from 0-2
    c = random.randint(0,4)                          #random c from 0-2

    if (playerBoard[r][c] == "X"):                     #if ship in that spot
        playerBoard[r][c] = "!"
        print("Computer hit your ship")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\explosion.wav')

    elif (playerBoard[r][c] == "*") or (playerBoard[r][c] == "!"):                  #if spot already taken
        playerChoice(playerBoard)
    else:
        playerBoard[r][c] = "*"                                 #put an * in the spot chosen

    return playerBoard


def winGame(playerBoard, compBoard):
    """
    Conditions to win the game
    Arguments:
        playerBoard: the player's board
        compBoard: the computer's board
    Returns:
        Determine if there's a winner
    """

    if (playerBoard[0][0] != "X") and (playerBoard[0][1] != "X") and (playerBoard[0][2] != "X")and (playerBoard[0][3] != "X") and (playerBoard[0][4] != "X") and (playerBoard[1][0] != "X") and (playerBoard[1][1] != "X") and (playerBoard[1][2] != "X") and (playerBoard[1][3] != "X") and (playerBoard[1][4] != "X") and (playerBoard[2][0] != "X") and (playerBoard[2][1] != "X") and (playerBoard[2][2] != "X") and (playerBoard[2][3] != "X") and (playerBoard[2][4] != "X") and (playerBoard[3][0] != "X") and (playerBoard[3][1] != "X")and (playerBoard[3][2] != "X") and (playerBoard[3][3] != "X") and (playerBoard[3][4] != "X") and (playerBoard[4][0] != "X") and (playerBoard[4][1] != "X") and (playerBoard[4][2] != "X")and (playerBoard[4][3] != "X") and (playerBoard[4][4] != "X"):
        print("Computer wins")       #if all the X's are hit on the player's board
        return 1

    elif (compBoard[0][0] != "X") and (compBoard[0][1] != "X") and (compBoard[0][2] != "X") and (compBoard[0][3] != "X") and (compBoard[0][4] != "X") and (compBoard[1][0] != "X") and (compBoard[1][1] != "X") and (compBoard[1][2] != "X") and (compBoard[1][3] != "X") and (compBoard[1][4] != "X") and (compBoard[2][0] != "X") and (compBoard[2][1] != "X") and (compBoard[2][2] != "X") and (compBoard[2][3] != "X") and (compBoard[2][4] != "X") and (compBoard[3][0] != "X") and (compBoard[3][1] != "X")and (compBoard[3][2] != "X") and (compBoard[3][3] != "X") and (compBoard[3][4] != "X") and (compBoard[4][0] != "X") and (compBoard[4][1] != "X") and (compBoard[4][2] != "X")and (compBoard[4][3] != "X") and (compBoard[4][4] != "X"):
        print("You win!")                #if all the X's are hit on the computer's board
        return 1

    else:
        return 0

def doneGame():
    """
    End the game or start new game
    Arguments:
        N/A
    Returns:
        game over or new game
    """
    ask = input("Play again? 1 for yes, 2 for no")

    if ask == 1:                  #play again
        main()
    elif ask == 2:                 #don't play again
        print("Okay, bye!")
    else:
        print("Invalid. Enter 1 for yes or 2 for no")
        doneGame()


def main():
    """
    Play a game of Battleship
    Arguments:
        N/A
    Returns:
        N/A
    """

    game = 0
    playerScore = 0                 #player's initial score
    compScore = 0                  #computer's initial score

    print("Let's play Battleship!")

    playerBoard = [["[]","[]","[]","[]","[]"],
             ["[]","[]","[]","[]","[]"],
             ["[]","[]","[]","[]","[]"],
             ["[]","[]","[]","[]","[]"],
             ["[]","[]","[]","[]","[]"]]

    compBoard = [["[]","[]","[]","[]","[]"],
             ["[]","[]","[]","[]","[]"],
             ["[]","[]","[]","[]","[]"],
             ["[]","[]","[]","[]","[]"],
             ["[]","[]","[]","[]","[]"]]


    playerBoard = startBoard(playerBoard)
    compBoard = startBoard(compBoard)
    printBoard(playerBoard)
    #print("")
    #printBoard(compBoard)

    turns = 10

    while turns > 0 :
        while game == 0:
            compBoard = playerChoice(compBoard)
            game = winGame(playerBoard, compBoard)
            #changeBoard(compBoard, game)

            playerBoard = computerChoice(playerBoard)
            game = winGame(playerBoard, compBoard)
            changeBoard(playerBoard, game)
            compScore

            turns -= 1

            print(turns,"turns left")


if __name__ == '__main__':
    main()