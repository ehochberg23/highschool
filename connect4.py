'''
Created on Jan 24, 2023

@author: EHochberg23
'''

import random
from playsound import playsound
import emoji

PLAYERPIECE = "🔺"
COMPPIECE = "⚫"
SPOT = "⬛"


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


def playerChoice(board):
    """
    The player's choice of where to place their piece
    Arguments:
        board: the board
    Returns:
        A triangle in the spot that the player chose
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

    if c < 0 or c > 6 or r < 0 or r > 5:  # if column smaller than 0 or bigger than 6 or row smaller than 0 or bigger than 5
        print("Please enter valid numbers")
        playerChoice(board)


    elif (board[r][c] == PLAYERPIECE) or (board[r][c] == COMPPIECE):  # if spot already taken
        print("Spot taken. Choose again")
        playerChoice(board)

    elif (r < 5 and board[(r + 1)][c] == SPOT):
        print("Cannot place a piece above an empty spot. Choose again")  # if spot underneath is open
        playerChoice(board)

    else:
        board[r][c] = PLAYERPIECE  # put a piece where the player chose
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\pop.wav')

    return board


def computerChoice(board):
    """
    Randomize the computer's choice of where to put down a piece
    Arguments:
        board: the board
    Returns:
        An circle on the board in the spot chosen
    """

    r = random.randint(0, 5)  # random r from 0-5
    c = random.randint(0, 6)  # random c from 0-6

    if (board[r][c] == PLAYERPIECE) or (board[r][c] == COMPPIECE):  # if spot already taken
        computerChoice(board)
    elif (r < 5 and board[r + 1][c] == SPOT):  # if spot underneath is open
        computerChoice(board)
    else:
        board[r][c] = COMPPIECE  # put an O in the spot chosen
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\pop.wav')

    return board


def winGame(board):
    """
    Conditions to win the game
    Arguments:
        board: the board
    Returns:
        end game if there's a winner
    """

    # across wins

    # row 0
    if (board[0][0] == COMPPIECE) and (board[0][1] == COMPPIECE) and (board[0][2] == COMPPIECE) and (
            board[0][3] == COMPPIECE):
        print("Computer wins")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1
    elif (board[0][1] == COMPPIECE) and (board[0][2] == COMPPIECE) and (board[0][3] == COMPPIECE) and (
            board[0][4] == COMPPIECE):
        print("Computer wins")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1
    elif (board[0][2] == COMPPIECE) and (board[0][3] == COMPPIECE) and (board[0][4] == COMPPIECE) and (
            board[0][5] == COMPPIECE):
        print("Computer wins")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1
    elif (board[0][3] == COMPPIECE) and (board[0][4] == COMPPIECE) and (board[0][5] == COMPPIECE) and (
            board[0][6] == COMPPIECE):
        print("Computer wins")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1

    elif (board[0][0] == PLAYERPIECE) and (board[0][1] == PLAYERPIECE) and (board[0][2] == PLAYERPIECE) and (
            board[0][3] == PLAYERPIECE):
        print("You win")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1
    elif (board[0][1] == PLAYERPIECE) and (board[0][2] == PLAYERPIECE) and (board[0][3] == PLAYERPIECE) and (
            board[0][4] == PLAYERPIECE):
        print("You win")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1
    elif (board[0][2] == PLAYERPIECE) and (board[0][3] == PLAYERPIECE) and (board[0][4] == PLAYERPIECE) and (
            board[0][5] == PLAYERPIECE):
        print("You win")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1
    elif (board[0][3] == PLAYERPIECE) and (board[0][4] == PLAYERPIECE) and (board[0][5] == PLAYERPIECE) and (
            board[0][6] == PLAYERPIECE):
        print("You win")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1

        # row 1
    elif (board[1][0] == COMPPIECE) and (board[1][1] == COMPPIECE) and (board[1][2] == COMPPIECE) and (
            board[1][3] == COMPPIECE):
        print("Computer wins")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1
    elif (board[1][1] == COMPPIECE) and (board[1][2] == COMPPIECE) and (board[1][3] == COMPPIECE) and (
            board[1][4] == COMPPIECE):
        print("Computer wins")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1
    elif (board[1][2] == COMPPIECE) and (board[1][3] == COMPPIECE) and (board[1][4] == COMPPIECE) and (
            board[1][5] == COMPPIECE):
        print("Computer wins")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1
    elif (board[1][3] == COMPPIECE) and (board[1][4] == COMPPIECE) and (board[1][5] == COMPPIECE) and (
            board[1][6] == COMPPIECE):
        print("Computer wins")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1

    elif (board[1][0] == PLAYERPIECE) and (board[1][1] == PLAYERPIECE) and (board[1][2] == PLAYERPIECE) and (
            board[1][3] == PLAYERPIECE):
        print("You win")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1
    elif (board[1][1] == PLAYERPIECE) and (board[1][2] == PLAYERPIECE) and (board[1][3] == PLAYERPIECE) and (
            board[1][4] == PLAYERPIECE):
        print("You win")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1
    elif (board[1][2] == PLAYERPIECE) and (board[1][3] == PLAYERPIECE) and (board[1][4] == PLAYERPIECE) and (
            board[1][5] == PLAYERPIECE):
        print("You win")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1
    elif (board[1][3] == PLAYERPIECE) and (board[1][4] == PLAYERPIECE) and (board[1][5] == PLAYERPIECE) and (
            board[1][6] == PLAYERPIECE):
        print("You win")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1

        # row 2
    elif (board[2][0] == COMPPIECE) and (board[2][1] == COMPPIECE) and (board[2][2] == COMPPIECE) and (
            board[2][3] == COMPPIECE):
        print("Computer wins")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1
    elif (board[2][1] == COMPPIECE) and (board[2][2] == COMPPIECE) and (board[2][3] == COMPPIECE) and (
            board[2][4] == COMPPIECE):
        print("Computer wins")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1
    elif (board[2][2] == COMPPIECE) and (board[2][3] == COMPPIECE) and (board[2][4] == COMPPIECE) and (
            board[2][5] == COMPPIECE):
        print("Computer wins")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1
    elif (board[2][3] == COMPPIECE) and (board[2][4] == COMPPIECE) and (board[2][5] == COMPPIECE) and (
            board[2][6] == COMPPIECE):
        print("Computer wins")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1

    elif (board[2][0] == PLAYERPIECE) and (board[2][1] == PLAYERPIECE) and (board[2][2] == PLAYERPIECE) and (
            board[2][3] == PLAYERPIECE):
        print("You win")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1
    elif (board[2][1] == PLAYERPIECE) and (board[2][2] == PLAYERPIECE) and (board[2][3] == PLAYERPIECE) and (
            board[2][4] == PLAYERPIECE):
        print("You win")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1
    elif (board[2][2] == PLAYERPIECE) and (board[2][3] == PLAYERPIECE) and (board[2][4] == PLAYERPIECE) and (
            board[2][5] == PLAYERPIECE):
        print("You win")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1
    elif (board[2][3] == PLAYERPIECE) and (board[2][4] == PLAYERPIECE) and (board[2][5] == PLAYERPIECE) and (
            board[2][6] == PLAYERPIECE):
        print("You win")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1

        # row 3
    elif (board[3][0] == COMPPIECE) and (board[3][1] == COMPPIECE) and (board[3][2] == COMPPIECE) and (
            board[3][3] == COMPPIECE):
        print("Computer wins")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1
    elif (board[3][1] == COMPPIECE) and (board[3][2] == COMPPIECE) and (board[3][3] == COMPPIECE) and (
            board[3][4] == COMPPIECE):
        print("Computer wins")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1
    elif (board[3][2] == COMPPIECE) and (board[3][3] == COMPPIECE) and (board[3][4] == COMPPIECE) and (
            board[3][5] == COMPPIECE):
        print("Computer wins")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1
    elif (board[3][3] == COMPPIECE) and (board[3][4] == COMPPIECE) and (board[3][5] == COMPPIECE) and (
            board[3][6] == COMPPIECE):
        print("Computer wins")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1

    elif (board[3][0] == PLAYERPIECE) and (board[3][1] == PLAYERPIECE) and (board[3][2] == PLAYERPIECE) and (
            board[3][3] == PLAYERPIECE):
        print("You win")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1
    elif (board[3][1] == PLAYERPIECE) and (board[3][2] == PLAYERPIECE) and (board[3][3] == PLAYERPIECE) and (
            board[3][4] == PLAYERPIECE):
        print("You win")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1
    elif (board[3][2] == PLAYERPIECE) and (board[3][3] == PLAYERPIECE) and (board[3][4] == PLAYERPIECE) and (
            board[3][5] == PLAYERPIECE):
        print("You win")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1
    elif (board[3][3] == PLAYERPIECE) and (board[3][4] == PLAYERPIECE) and (board[3][5] == PLAYERPIECE) and (
            board[3][6] == PLAYERPIECE):
        print("You win")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1

        # row 4
    elif (board[4][0] == COMPPIECE) and (board[4][1] == COMPPIECE) and (board[4][2] == COMPPIECE) and (
            board[4][3] == COMPPIECE):
        print("Computer wins")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1
    elif (board[4][1] == COMPPIECE) and (board[4][2] == COMPPIECE) and (board[4][3] == COMPPIECE) and (
            board[4][4] == COMPPIECE):
        print("Computer wins")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1
    elif (board[4][2] == COMPPIECE) and (board[4][3] == COMPPIECE) and (board[4][4] == COMPPIECE) and (
            board[4][5] == COMPPIECE):
        print("Computer wins")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1
    elif (board[4][3] == COMPPIECE) and (board[4][4] == COMPPIECE) and (board[4][5] == COMPPIECE) and (
            board[4][6] == COMPPIECE):
        print("Computer wins")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1

    elif (board[4][0] == PLAYERPIECE) and (board[4][1] == PLAYERPIECE) and (board[4][2] == PLAYERPIECE) and (
            board[4][3] == PLAYERPIECE):
        print("You win")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1
    elif (board[4][1] == PLAYERPIECE) and (board[4][2] == PLAYERPIECE) and (board[4][3] == PLAYERPIECE) and (
            board[4][4] == PLAYERPIECE):
        print("You win")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1
    elif (board[4][2] == PLAYERPIECE) and (board[4][3] == PLAYERPIECE) and (board[4][4] == PLAYERPIECE) and (
            board[4][5] == PLAYERPIECE):
        print("You win")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1
    elif (board[4][3] == PLAYERPIECE) and (board[4][4] == PLAYERPIECE) and (board[4][5] == PLAYERPIECE) and (
            board[4][6] == PLAYERPIECE):
        print("You win")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1

        # row 5
    elif (board[5][0] == COMPPIECE) and (board[5][1] == COMPPIECE) and (board[5][2] == COMPPIECE) and (
            board[5][3] == COMPPIECE):
        print("Computer wins")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1
    elif (board[5][1] == COMPPIECE) and (board[5][2] == COMPPIECE) and (board[5][3] == COMPPIECE) and (
            board[5][4] == COMPPIECE):
        print("Computer wins")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1
    elif (board[5][2] == COMPPIECE) and (board[5][3] == COMPPIECE) and (board[5][4] == COMPPIECE) and (
            board[5][5] == COMPPIECE):
        print("Computer wins")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1
    elif (board[5][3] == COMPPIECE) and (board[5][4] == COMPPIECE) and (board[5][5] == COMPPIECE) and (
            board[5][6] == COMPPIECE):
        print("Computer wins")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1

    elif (board[5][0] == PLAYERPIECE) and (board[5][1] == PLAYERPIECE) and (board[5][2] == PLAYERPIECE) and (
            board[5][3] == PLAYERPIECE):
        print("You win")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1
    elif (board[5][1] == PLAYERPIECE) and (board[5][2] == PLAYERPIECE) and (board[5][3] == PLAYERPIECE) and (
            board[5][4] == PLAYERPIECE):
        print("You win")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1
    elif (board[5][2] == PLAYERPIECE) and (board[5][3] == PLAYERPIECE) and (board[5][4] == PLAYERPIECE) and (
            board[5][5] == PLAYERPIECE):
        print("You win")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1
    elif (board[5][3] == PLAYERPIECE) and (board[5][4] == PLAYERPIECE) and (board[5][5] == PLAYERPIECE) and (
            board[5][6] == PLAYERPIECE):
        print("You win")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1

    # down wins

    # column 0
    elif board[0][0] == COMPPIECE and board[1][0] == COMPPIECE and board[2][0] == COMPPIECE and board[3][
        0] == COMPPIECE:
        print("Computer wins")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1
    elif board[1][0] == COMPPIECE and board[2][0] == COMPPIECE and board[3][0] == COMPPIECE and board[4][
        0] == COMPPIECE:
        print("Computer wins")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1
    elif board[2][0] == COMPPIECE and board[3][0] == COMPPIECE and board[4][0] == COMPPIECE and board[5][
        0] == COMPPIECE:
        print("Computer wins")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1

    elif board[0][0] == PLAYERPIECE and board[1][0] == PLAYERPIECE and board[2][0] == PLAYERPIECE and board[3][
        0] == PLAYERPIECE:
        print("You win")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1
    elif board[1][0] == PLAYERPIECE and board[2][0] == PLAYERPIECE and board[3][0] == PLAYERPIECE and board[4][
        0] == PLAYERPIECE:
        print("You win")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1
    elif board[2][0] == PLAYERPIECE and board[3][0] == PLAYERPIECE and board[4][0] == PLAYERPIECE and board[5][
        0] == PLAYERPIECE:
        print("You win")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1

        # column 1
    elif board[0][1] == COMPPIECE and board[1][1] == COMPPIECE and board[2][1] == COMPPIECE and board[3][
        1] == COMPPIECE:
        print("Computer wins")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1
    elif board[1][1] == COMPPIECE and board[2][1] == COMPPIECE and board[3][1] == COMPPIECE and board[4][
        1] == COMPPIECE:
        print("Computer wins")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1
    elif board[2][1] == COMPPIECE and board[3][1] == COMPPIECE and board[4][1] == COMPPIECE and board[5][
        1] == COMPPIECE:
        print("Computer wins")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1

    elif board[0][1] == PLAYERPIECE and board[1][1] == PLAYERPIECE and board[2][1] == PLAYERPIECE and board[3][
        1] == PLAYERPIECE:
        print("You win")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1
    elif board[1][1] == PLAYERPIECE and board[2][1] == PLAYERPIECE and board[3][1] == PLAYERPIECE and board[4][
        1] == PLAYERPIECE:
        print("You win")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1
    elif board[2][1] == PLAYERPIECE and board[3][1] == PLAYERPIECE and board[4][1] == PLAYERPIECE and board[5][
        1] == PLAYERPIECE:
        print("You win")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1

        # column 2
    elif board[0][2] == COMPPIECE and board[1][2] == COMPPIECE and board[2][2] == COMPPIECE and board[3][
        2] == COMPPIECE:
        print("Computer wins")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1
    elif board[1][2] == COMPPIECE and board[2][2] == COMPPIECE and board[3][2] == COMPPIECE and board[4][
        2] == COMPPIECE:
        print("Computer wins")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1
    elif board[2][2] == COMPPIECE and board[3][2] == COMPPIECE and board[4][2] == COMPPIECE and board[5][
        2] == COMPPIECE:
        print("Computer wins")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1

    elif board[0][2] == PLAYERPIECE and board[1][2] == PLAYERPIECE and board[2][2] == PLAYERPIECE and board[3][
        2] == PLAYERPIECE:
        print("You win")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1
    elif board[1][2] == PLAYERPIECE and board[2][2] == PLAYERPIECE and board[3][2] == PLAYERPIECE and board[4][
        2] == PLAYERPIECE:
        print("You win")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1
    elif board[2][2] == PLAYERPIECE and board[3][2] == PLAYERPIECE and board[4][2] == PLAYERPIECE and board[5][
        2] == PLAYERPIECE:
        print("You win")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1

        # column 3
    elif board[0][3] == COMPPIECE and board[1][3] == COMPPIECE and board[2][3] == COMPPIECE and board[3][
        3] == COMPPIECE:
        print("Computer wins")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1
    elif board[1][3] == COMPPIECE and board[2][3] == COMPPIECE and board[3][3] == COMPPIECE and board[4][
        3] == COMPPIECE:
        print("Computer wins")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1
    elif board[2][3] == COMPPIECE and board[3][3] == COMPPIECE and board[4][3] == COMPPIECE and board[5][
        3] == COMPPIECE:
        print("Computer wins")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1

    elif board[0][3] == PLAYERPIECE and board[1][3] == PLAYERPIECE and board[2][3] == PLAYERPIECE and board[3][
        3] == PLAYERPIECE:
        print("You win")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1
    elif board[1][3] == PLAYERPIECE and board[2][3] == PLAYERPIECE and board[3][3] == PLAYERPIECE and board[4][
        3] == PLAYERPIECE:
        print("You win")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1
    elif board[2][3] == PLAYERPIECE and board[3][3] == PLAYERPIECE and board[4][3] == PLAYERPIECE and board[5][
        3] == PLAYERPIECE:
        print("You win")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1

        # column 4
    elif board[0][4] == COMPPIECE and board[1][4] == COMPPIECE and board[2][4] == COMPPIECE and board[3][
        4] == COMPPIECE:
        print("Computer wins")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1
    elif board[1][4] == COMPPIECE and board[2][4] == COMPPIECE and board[3][4] == COMPPIECE and board[4][
        4] == COMPPIECE:
        print("Computer wins")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1
    elif board[2][4] == COMPPIECE and board[3][4] == COMPPIECE and board[4][4] == COMPPIECE and board[5][
        4] == COMPPIECE:
        print("Computer wins")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1

    elif board[0][4] == PLAYERPIECE and board[1][4] == PLAYERPIECE and board[2][4] == PLAYERPIECE and board[3][
        4] == PLAYERPIECE:
        print("You win")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1
    elif board[1][4] == PLAYERPIECE and board[2][4] == PLAYERPIECE and board[3][4] == PLAYERPIECE and board[4][
        4] == PLAYERPIECE:
        print("You win")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1
    elif board[2][4] == PLAYERPIECE and board[3][4] == PLAYERPIECE and board[4][4] == PLAYERPIECE and board[5][
        4] == PLAYERPIECE:
        print("You win")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1

        # column 5
    elif board[0][5] == COMPPIECE and board[1][5] == COMPPIECE and board[2][5] == COMPPIECE and board[3][
        5] == COMPPIECE:
        print("Computer wins")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1
    elif board[1][5] == COMPPIECE and board[2][5] == COMPPIECE and board[3][5] == COMPPIECE and board[4][
        5] == COMPPIECE:
        print("Computer wins")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1
    elif board[2][5] == COMPPIECE and board[3][5] == COMPPIECE and board[4][5] == COMPPIECE and board[5][
        5] == COMPPIECE:
        print("Computer wins")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1

    elif board[0][5] == PLAYERPIECE and board[1][5] == PLAYERPIECE and board[2][5] == PLAYERPIECE and board[3][
        5] == PLAYERPIECE:
        print("You win")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1
    elif board[1][5] == PLAYERPIECE and board[2][5] == PLAYERPIECE and board[3][5] == PLAYERPIECE and board[4][
        5] == PLAYERPIECE:
        print("You win")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1
    elif board[2][5] == PLAYERPIECE and board[3][5] == PLAYERPIECE and board[4][5] == PLAYERPIECE and board[5][
        5] == PLAYERPIECE:
        print("You win")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1

        # column 6
    elif board[0][6] == COMPPIECE and board[1][6] == COMPPIECE and board[2][6] == COMPPIECE and board[3][
        6] == COMPPIECE:
        print("Computer wins")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1
    elif board[1][6] == COMPPIECE and board[2][6] == COMPPIECE and board[3][6] == COMPPIECE and board[4][
        6] == COMPPIECE:
        print("Computer wins")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1
    elif board[2][6] == COMPPIECE and board[3][6] == COMPPIECE and board[4][6] == COMPPIECE and board[5][
        6] == COMPPIECE:
        print("Computer wins")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1

    elif board[0][6] == PLAYERPIECE and board[1][6] == PLAYERPIECE and board[2][6] == PLAYERPIECE and board[3][
        6] == PLAYERPIECE:
        print("You win")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1
    elif board[1][6] == PLAYERPIECE and board[2][6] == PLAYERPIECE and board[3][6] == PLAYERPIECE and board[4][
        6] == PLAYERPIECE:
        print("You win")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1
    elif board[2][6] == PLAYERPIECE and board[3][6] == PLAYERPIECE and board[4][6] == PLAYERPIECE and board[5][
        6] == PLAYERPIECE:
        print("You win")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1

    # right diagonal wins

    # row 0
    elif (board[0][0] == COMPPIECE) and (board[1][1] == COMPPIECE) and (board[2][2] == COMPPIECE) and board[3][
        3] == COMPPIECE:
        print("Computer wins")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1
    elif (board[0][1] == COMPPIECE) and (board[1][2] == COMPPIECE) and (board[2][3] == COMPPIECE) and board[3][
        4] == COMPPIECE:
        print("Computer wins")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1
    elif (board[0][2] == COMPPIECE) and (board[1][3] == COMPPIECE) and (board[2][4] == COMPPIECE) and board[3][
        5] == COMPPIECE:
        print("Computer wins")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1
    elif (board[0][3] == COMPPIECE) and (board[1][4] == COMPPIECE) and (board[2][5] == COMPPIECE) and board[3][
        6] == COMPPIECE:
        print("Computer wins")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1

    elif (board[0][0] == PLAYERPIECE) and (board[1][1] == PLAYERPIECE) and (board[2][2] == PLAYERPIECE) and board[3][
        3] == PLAYERPIECE:
        print("You win")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1
    elif (board[0][1] == PLAYERPIECE) and (board[1][2] == PLAYERPIECE) and (board[2][3] == PLAYERPIECE) and board[3][
        4] == PLAYERPIECE:
        print("You win")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1
    elif (board[0][2] == PLAYERPIECE) and (board[1][3] == PLAYERPIECE) and (board[2][4] == PLAYERPIECE) and board[3][
        5] == PLAYERPIECE:
        print("You win")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1
    elif (board[0][3] == PLAYERPIECE) and (board[1][4] == PLAYERPIECE) and (board[2][5] == PLAYERPIECE) and board[3][
        6] == PLAYERPIECE:
        print("You win")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1

        # row 1
    elif (board[1][0] == COMPPIECE) and (board[2][1] == COMPPIECE) and (board[3][2] == COMPPIECE) and board[4][
        3] == COMPPIECE:
        print("Computer wins")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1
    elif (board[1][1] == COMPPIECE) and (board[2][2] == COMPPIECE) and (board[3][3] == COMPPIECE) and board[4][
        4] == COMPPIECE:
        print("Computer wins")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1
    elif (board[1][2] == COMPPIECE) and (board[2][3] == COMPPIECE) and (board[3][4] == COMPPIECE) and board[4][
        5] == COMPPIECE:
        print("Computer wins")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1
    elif (board[1][3] == COMPPIECE) and (board[2][4] == COMPPIECE) and (board[3][5] == COMPPIECE) and board[4][
        6] == COMPPIECE:
        print("Computer wins")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1

    elif (board[1][0] == PLAYERPIECE) and (board[2][1] == PLAYERPIECE) and (board[3][2] == PLAYERPIECE) and board[4][
        3] == PLAYERPIECE:
        print("You win")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1
    elif (board[1][1] == PLAYERPIECE) and (board[2][2] == PLAYERPIECE) and (board[3][3] == PLAYERPIECE) and board[4][
        4] == PLAYERPIECE:
        print("You win")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1
    elif (board[1][2] == PLAYERPIECE) and (board[2][3] == PLAYERPIECE) and (board[3][4] == PLAYERPIECE) and board[4][
        5] == PLAYERPIECE:
        print("You win")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1
    elif (board[1][3] == PLAYERPIECE) and (board[2][4] == PLAYERPIECE) and (board[3][5] == PLAYERPIECE) and board[4][
        6] == PLAYERPIECE:
        print("You win")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1

        # row 2
    elif (board[2][0] == COMPPIECE) and (board[3][1] == COMPPIECE) and (board[4][2] == COMPPIECE) and board[5][
        3] == COMPPIECE:
        print("Computer wins")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1
    elif (board[2][1] == COMPPIECE) and (board[3][2] == COMPPIECE) and (board[4][3] == COMPPIECE) and board[5][
        4] == COMPPIECE:
        print("Computer wins")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1
    elif (board[2][2] == COMPPIECE) and (board[3][3] == COMPPIECE) and (board[4][4] == COMPPIECE) and board[5][
        5] == COMPPIECE:
        print("Computer wins")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1
    elif (board[2][3] == COMPPIECE) and (board[3][4] == COMPPIECE) and (board[4][5] == COMPPIECE) and board[5][
        6] == COMPPIECE:
        print("Computer wins")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1

    elif (board[2][0] == PLAYERPIECE) and (board[3][1] == PLAYERPIECE) and (board[4][2] == PLAYERPIECE) and board[5][
        3] == PLAYERPIECE:
        print("You win")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1
    elif (board[2][1] == PLAYERPIECE) and (board[3][2] == PLAYERPIECE) and (board[4][3] == PLAYERPIECE) and board[5][
        4] == PLAYERPIECE:
        print("You win")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1
    elif (board[2][2] == PLAYERPIECE) and (board[3][3] == PLAYERPIECE) and (board[4][4] == PLAYERPIECE) and board[5][
        5] == PLAYERPIECE:
        print("You win")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1
    elif (board[2][3] == PLAYERPIECE) and (board[3][4] == PLAYERPIECE) and (board[4][5] == PLAYERPIECE) and board[5][
        6] == PLAYERPIECE:
        print("You win")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1



    # left diagonal wins

    # row 5
    elif board[5][0] == COMPPIECE and board[4][1] == COMPPIECE and board[3][2] == COMPPIECE and board[2][
        3] == COMPPIECE:
        print("Computer wins")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1
    elif board[5][1] == COMPPIECE and board[4][2] == COMPPIECE and board[3][3] == COMPPIECE and board[2][
        4] == COMPPIECE:
        print("Computer wins")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1
    elif board[5][2] == COMPPIECE and board[4][3] == COMPPIECE and board[3][4] == COMPPIECE and board[2][
        5] == COMPPIECE:
        print("Computer wins")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1
    elif board[5][3] == COMPPIECE and board[4][4] == COMPPIECE and board[3][5] == COMPPIECE and board[2][
        6] == COMPPIECE:
        print("Computer wins")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1

    elif board[5][0] == PLAYERPIECE and board[4][1] == PLAYERPIECE and board[3][2] == PLAYERPIECE and board[2][
        3] == PLAYERPIECE:
        print("You win")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1
    elif board[5][1] == PLAYERPIECE and board[4][2] == PLAYERPIECE and board[3][3] == PLAYERPIECE and board[2][
        4] == PLAYERPIECE:
        print("You win")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1
    elif board[5][2] == PLAYERPIECE and board[4][3] == PLAYERPIECE and board[3][4] == PLAYERPIECE and board[2][
        5] == PLAYERPIECE:
        print("You win")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1
    elif board[5][3] == PLAYERPIECE and board[4][4] == PLAYERPIECE and board[3][5] == PLAYERPIECE and board[2][
        6] == PLAYERPIECE:
        print("You win")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1

        # row 4
    elif board[4][0] == COMPPIECE and board[3][1] == COMPPIECE and board[2][2] == COMPPIECE and board[1][
        3] == COMPPIECE:
        print("Computer wins")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1
    elif board[4][1] == COMPPIECE and board[3][2] == COMPPIECE and board[2][3] == COMPPIECE and board[1][
        4] == COMPPIECE:
        print("Computer wins")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1
    elif board[4][2] == COMPPIECE and board[3][3] == COMPPIECE and board[2][4] == COMPPIECE and board[1][
        5] == COMPPIECE:
        print("Computer wins")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1
    elif board[4][3] == COMPPIECE and board[3][4] == COMPPIECE and board[2][5] == COMPPIECE and board[1][
        6] == COMPPIECE:
        print("Computer wins")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1

    elif board[4][0] == PLAYERPIECE and board[3][1] == PLAYERPIECE and board[2][2] == PLAYERPIECE and board[1][
        3] == PLAYERPIECE:
        print("You win")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1
    elif board[4][1] == PLAYERPIECE and board[3][2] == PLAYERPIECE and board[2][3] == PLAYERPIECE and board[1][
        4] == PLAYERPIECE:
        print("You win")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1
    elif board[4][2] == PLAYERPIECE and board[3][3] == PLAYERPIECE and board[2][4] == PLAYERPIECE and board[1][
        5] == PLAYERPIECE:
        print("You win")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1
    elif board[4][3] == PLAYERPIECE and board[3][4] == PLAYERPIECE and board[2][5] == PLAYERPIECE and board[1][
        6] == PLAYERPIECE:
        print("You win")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1

        # row 3
    elif board[3][0] == COMPPIECE and board[2][1] == COMPPIECE and board[1][2] == COMPPIECE and board[0][
        3] == COMPPIECE:
        print("Computer wins")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1
    elif board[3][1] == COMPPIECE and board[2][2] == COMPPIECE and board[1][3] == COMPPIECE and board[0][
        4] == COMPPIECE:
        print("Computer wins")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1
    elif board[3][2] == COMPPIECE and board[2][3] == COMPPIECE and board[1][4] == COMPPIECE and board[0][
        5] == COMPPIECE:
        print("Computer wins")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1
    elif board[3][3] == COMPPIECE and board[2][4] == COMPPIECE and board[1][5] == COMPPIECE and board[0][
        6] == COMPPIECE:
        print("Computer wins")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1

    elif board[3][0] == PLAYERPIECE and board[2][1] == PLAYERPIECE and board[1][2] == PLAYERPIECE and board[0][
        3] == PLAYERPIECE:
        print("You win")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1
    elif board[3][1] == PLAYERPIECE and board[2][2] == PLAYERPIECE and board[1][3] == PLAYERPIECE and board[0][
        4] == PLAYERPIECE:
        print("You win")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1
    elif board[3][2] == PLAYERPIECE and board[2][3] == PLAYERPIECE and board[1][4] == PLAYERPIECE and board[0][
        5] == PLAYERPIECE:
        print("You win")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1
    elif board[3][3] == PLAYERPIECE and board[2][4] == PLAYERPIECE and board[1][5] == PLAYERPIECE and board[0][
        6] == PLAYERPIECE:
        print("You win")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
        return 1

    elif (board[0][0] != SPOT) and (board[0][1] != SPOT) and (board[0][2] != SPOT) and (board[0][3] != SPOT) and (
            board[0][4] != SPOT) and (board[0][5] != SPOT) and (board[0][6] != SPOT) and (
            board[1][0] != SPOT) and (board[1][1] != SPOT) and (board[1][2] != SPOT) and (board[1][3] != SPOT) and (
            board[1][4] != SPOT) and (board[1][5] != SPOT) and (board[1][6] != SPOT) and (
            board[2][0] != SPOT) and (board[2][1] != SPOT) and (board[2][2] != SPOT) and (board[2][3] != SPOT) and (
            board[2][4] != SPOT) and (board[2][5] != SPOT) and (board[2][6] != SPOT) and (
            board[3][0] != SPOT) and (board[3][1] != SPOT) and (board[3][2] != SPOT) and (board[3][3] != SPOT) and (
            board[3][4] != SPOT) and (board[3][5] != SPOT) and (board[3][6] != SPOT) and (
            board[4][0] != SPOT) and (board[4][1] != SPOT) and (board[4][2] != SPOT) and (board[4][3] != SPOT) and (
            board[4][4] != SPOT) and (board[4][5] != SPOT) and (board[4][6] != SPOT) and (
            board[5][0] != SPOT) and (board[5][1] != SPOT) and (board[5][2] != SPOT) and (board[5][3] != SPOT) and (
            board[5][4] != SPOT) and (board[5][5] != SPOT) and (board[5][6] != SPOT):
        print("Tie")
        playsound(r'G:\My Drive\Computer Science\CS2\Assignments\cheering.wav')
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
        exit()
    else:
        print("Invalid. Enter 1 for yes or 2 for no")
        doneGame()


def main():
    """
    Play a game of Connect 4
    Arguments:
        N/A
    Returns:
        N/A
    """
    game = 0

    print("Let's play Connect 4!")
    print("Your piece is a triangle, Computer's piece is a circle")
    print("Rows are 0-5 and columns are 0-6")

    board = [[SPOT, SPOT, SPOT, SPOT, SPOT, SPOT, SPOT],
             [SPOT, SPOT, SPOT, SPOT, SPOT, SPOT, SPOT],
             [SPOT, SPOT, SPOT, SPOT, SPOT, SPOT, SPOT],
             [SPOT, SPOT, SPOT, SPOT, SPOT, SPOT, SPOT],
             [SPOT, SPOT, SPOT, SPOT, SPOT, SPOT, SPOT],
             [SPOT, SPOT, SPOT, SPOT, SPOT, SPOT, SPOT]]

    printBoard(board)

    while game == 0:
        board = playerChoice(board)
        game = winGame(board)
        changeBoard(board, game)

        board = computerChoice(board)
        game = winGame(board)
        changeBoard(board, game)


if __name__ == "__main__":
    main()
