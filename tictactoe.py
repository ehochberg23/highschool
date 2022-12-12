"""
Name: Ellie Hochberg
Date: November 30, 2022
Description: Play a game of tic tac toe with computer
Bugs: No bugs
Plan:
    1) Show empty board
    2) Player chooses spot
    3) Computer chooses spot
    4) Repeat until winner is determined
"""

import random


def printBoard(board):
    """
    Print a board
    Arguments:
        board: the board
    Returns:
        An empty board
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
    The player's choice of where to put down an X
    Arguments:
        board: the board
    Returns:
        An X in the spot that the player chose
    """

    try:
        r = int(input("Pick a row"))  # row
        c = int(input("Pick a column"))  # column
    except:
        print("Error, please enter a valid number")

    if 0 > c > 2 or 0 > r > 2:  # if number smaller than 0 or bigger than 2
        print("Please enter valid numbers")
        playerChoice(board)


    elif (board[r][c] == "X") or (board[r][c] == "O"):  # if spot already taken
        print("Spot taken. Choose again")
        playerChoice(board)
    else:
        board[r][c] = "X"  # put an X where the player chose

    return board


def computerChoice(board):
    """
    Randomize the computer's choice of where to put an O
    Arguments:
        board: the board
    Returns:
        An O on the board in the spot chosen
    """

    r = random.randint(0, 2)  # random r from 0-2
    c = random.randint(0, 2)  # random c from 0-2

    if (board[r][c] == "X") or (board[r][c] == "O"):  # if spot already taken
        computerChoice(board)
    else:
        board[r][c] = "O"  # put an O in the spot chosen

    return board


def winGame(board):
    """
    Conditions to win the game
    Arguments:
        board: the board
    Returns:
        end game if there's a winner
    """

    if (board[0][0] == "X") and (board[0][1] == "X") and (board[0][2] == "X"):  # top across
        changeBoard(board)
        print("You win!")
        return 1

    elif (board[1][0] == "X") and (board[1][1] == "X") and (board[1][2] == "X"):  # middle across
        changeBoard(board)
        print("You win!")
        return 1

    elif (board[2][0] == "X") and (board[2][1] == "X") and (board[2][2] == "X"):  # bottom across
        print("You win!")
        return 1

    elif (board[0][0] == "X") and (board[1][1] == "X") and (board[2][2] == "X"):  # diagonal down
        print("You win!")
        return 1

    elif board[0][0] == "X" and board[1][0] == "X" and board[2][0] == "X":  # left down
        print("You win!")
        return 1

    elif board[0][1] == "X" and board[1][1] == "X" and board[2][1] == "X":  # middle down
        print("You win!")
        return 1

    elif board[0][2] == "X" and board[1][2] == "X" and board[2][2] == "X":  # right down
        print("You win!")
        return 1

    elif board[2][0] == "X" and board[1][1] == "X" and board[0][2] == "X":  # diagonal up
        print("You win")
        return 1

    elif (board[0][0] == "O") and (board[0][1] == "O") and (board[0][2] == "O"):  # top across
        print("Computer wins!")
        return 1

    elif (board[1][0] == "O") and (board[1][1] == "O") and (board[1][2] == "O"):  # middle across
        print("Computer wins!")
        return 1

    elif (board[2][0] == "O") and (board[2][1] == "O") and (board[2][2] == "O"):  # bottom across
        print("computer wins!")
        return 1

    elif (board[0][0] == "O") and (board[1][1] == "O") and (board[2][2] == "O"):  # diagonal down
        print("Computer wins!")
        return 1

    elif board[0][0] == "O" and board[1][0] == "O" and board[2][0] == "O":  # left down
        print("Computer wins!")
        return 1

    elif board[0][1] == "O" and board[1][1] == "O" and board[2][1] == "O":  # middle down
        print("Computer wins!")
        return 1

    elif board[0][2] == "O" and board[1][2] == "O" and board[2][2] == "O":  # right down
        print("Computer wins!")
        return 1

    elif board[2][0] == "O" and board[1][1] == "O" and board[0][2] == "O":  # diagonal up
        print("Computer wins!")
        return 1

    elif (board[0][0] != "#") and (board[0][1] != "#") and (board[0][2]) != "#" and (board[1][0] != "#") and (
            board[1][1] != "#") and (board[1][2] != "#") and (board[2][0] != "#") and (board[2][1] != "#") and (
            board[2][2] != "#"):
        print("Tie!")  # conditions to have a tie
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

    if ask == 1:  # play again
        main()
    elif ask == 2:  # don't play again
        print("Okay, bye!")
    else:
        print("Invalid. Enter 1 for yes or 2 for no")
        doneGame()


def main():
    """
    Play a game of tic tac toe
    Arguments:
        N/A
    Returns:
        N/A
    """
    game = 0

    print("let's play Tic Tac Toe!")
    print("You're X, Computer is O")

    board = [["#", "#", "#"],
             ["#", "#", "#"],
             ["#", "#", "#"]]

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