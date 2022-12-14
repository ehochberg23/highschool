"""
Name: Ellie Hochberg
Date: Dec 16, 2022
Description: Play a game of battleship with the computer
Bugs: No bugs
Plan:
    1)Generate a board for both the player and the computer with four randomly placed ships
    2)Ask the player where they want to shoot
    3)Put a 📍 if they didn't hit a ship and a 💥 if they did on the computer's board
    4)Computer shoots a random spot
    5)Put a 📍 if they didn't hit a ship and a 💥 if they did on the player's board
    6)Repeat until there is a winner
"""
import random
from playsound import playsound
import emoji

SHIP = "🚢"
BOOM = "💥"
MISS = "📍"
SPOT = "⬜"


def startBoard(board):
    """
    Generate a randomized board with 4 randomly placed ships
    Arguments:
        board: the randomly generated board
    Returns:
        The board with the 4 ships
    """
    i = 0
    while i < 4:  # run loop 4 times
        r = random.randint(0, 4)  # random number from 0-4
        c = random.randint(0, 4)  # random number from 0-4

        if board[r][c] == SHIP:  # if spot already chosen, try again
            continue
        else:
            board[r][c] = SHIP  # put an ship in that spot
            i += 1

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
            print(c, end="")
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
                print(c, end=" ")
            print()


def playerChoice(compBoard):
    """
    The player's choice of where to shoot
    Arguments:
        compBoard: the computer's board
    Returns:
        A pin emoji on the board if there is no ship in that spot
        An explosion emoji on the board if there is a ship in that spot
    """
    trying = True
    while trying:
        trying = False
        try:
            r = int(input("Pick a row"))  # row
            c = int(input("Pick a column"))  # column
        except:
            print("Please enter a number")
            trying = True

    if r < 0 or r > 4 or c < 0 or c > 4:        #if number greater than 4 or less than 0
        print("Choose a valid number")
        playerChoice(compBoard)

    elif (compBoard[r][c] == SHIP):  # if ship in that spot
        compBoard[r][c] = BOOM
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\explosion.wav')
        print("You hit a ship!")


    elif (compBoard[r][c] == MISS) or (compBoard[r][c] == BOOM):  # if spot already taken
        print("Spot already chosen. Choose again")
        playerChoice(compBoard)

    else:
        compBoard[r][c] = MISS  # put a pin emoji where the player chose
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\splash.wav')
        print("You did not hit a ship")

    return compBoard


def computerChoice(playerBoard):
    """
    Randomize the computer's choice of where to shoot
    Arguments:
        playerBoard: the player's board
    Returns:
        A pin emoji on the board if there is no ship in that spot
        An explosion emoji on the board if there is a ship in that spot
        """

    r = random.randint(0, 4)  # random r from 0-2
    c = random.randint(0, 4)  # random c from 0-2

    if (playerBoard[r][c] == SHIP):  # if ship in that spot
        playerBoard[r][c] = BOOM
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\explosion.wav')
        print("Computer hit your ship")

    elif (playerBoard[r][c] == MISS) or (playerBoard[r][c] == BOOM):  # if spot already taken
        playerChoice(playerBoard)
    else:
        playerBoard[r][c] = MISS         # put a pin emoji in the spot chosen
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\splash.wav')
        print("Computer did not hit a ship")


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

    if (playerBoard[0][0] != SHIP) and (playerBoard[0][1] != SHIP) and (playerBoard[0][2] != SHIP)and (playerBoard[0][3] != SHIP) and (playerBoard[0][4] != SHIP) and (playerBoard[1][0] != SHIP) and (playerBoard[1][1] != SHIP) and (playerBoard[1][2] != SHIP) and (playerBoard[1][3] != SHIP) and (playerBoard[1][4] != SHIP) and (playerBoard[2][0] != SHIP) and (playerBoard[2][1] != SHIP) and (playerBoard[2][2] != SHIP) and (playerBoard[2][3] != SHIP) and (playerBoard[2][4] != SHIP) and (playerBoard[3][0] != SHIP) and (playerBoard[3][1] != SHIP)and (playerBoard[3][2] != SHIP) and (playerBoard[3][3] != SHIP) and (playerBoard[3][4] != SHIP) and (playerBoard[4][0] != SHIP) and (playerBoard[4][1] != SHIP) and (playerBoard[4][2] != SHIP)and (playerBoard[4][3] != SHIP) and (playerBoard[4][4] != SHIP):
        print("Computer wins")  # if all the SHIP's are hit on the player's board
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\applause.wav')
        return 1

    elif (compBoard[0][0] != SHIP) and (compBoard[0][1] != SHIP) and (compBoard[0][2] != SHIP) and (compBoard[0][3] != SHIP) and (compBoard[0][4] != SHIP) and (compBoard[1][0] != SHIP) and (compBoard[1][1] != SHIP) and (compBoard[1][2] != SHIP) and (compBoard[1][3] != SHIP) and (compBoard[1][4] != SHIP) and (compBoard[2][0] != SHIP) and (compBoard[2][1] != SHIP) and (compBoard[2][2] != SHIP) and (compBoard[2][3] != SHIP) and (compBoard[2][4] != SHIP) and (compBoard[3][0] != SHIP) and (compBoard[3][1] != SHIP)and (compBoard[3][2] != SHIP) and (compBoard[3][3] != SHIP) and (compBoard[3][4] != SHIP) and (compBoard[4][0] != SHIP) and (compBoard[4][1] != SHIP) and (compBoard[4][2] != SHIP)and (compBoard[4][3] != SHIP) and (compBoard[4][4] != SHIP):
        print("You win!")  # if all the SHIP's are hit on the computer's board
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\applause.wav')
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
    going = True
    while going:
        going = False
        try:
            ask = int(input("Play again? 1 for yes, 2 for no"))
        except:
            print("Please enter 1 or 2")
            going = True

    if ask == 1:  # play again
        main()
    elif ask == 2:  # don't play again
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

    print("Let's play Battleship!\n")

    playerBoard = [[SPOT, SPOT, SPOT, SPOT, SPOT],
             [SPOT, SPOT, SPOT, SPOT, SPOT],
             [SPOT, SPOT, SPOT, SPOT, SPOT],
             [SPOT, SPOT, SPOT, SPOT, SPOT],
             [SPOT, SPOT, SPOT, SPOT, SPOT]]

    compBoard = [[SPOT, SPOT, SPOT, SPOT, SPOT],
             [SPOT, SPOT, SPOT, SPOT, SPOT],
             [SPOT, SPOT, SPOT, SPOT, SPOT],
             [SPOT, SPOT, SPOT, SPOT, SPOT],
             [SPOT, SPOT, SPOT, SPOT, SPOT]]

    playerBoard = startBoard(playerBoard)
    compBoard = startBoard(compBoard)
    printBoard(playerBoard)
    # print("")
    # printBoard(compBoard)

    turns = 10

    while turns > 0:
        while game == 0:
            compBoard = playerChoice(compBoard)
            game = winGame(playerBoard, compBoard)
            # changeBoard(compBoard, game)

            playerBoard = computerChoice(playerBoard)
            game = winGame(playerBoard, compBoard)
            changeBoard(playerBoard, game)

            turns -= 1

            print(turns, "turns left")


if __name__ == '__main__':
    main()
