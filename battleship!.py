"""
Name: Ellie Hochberg
Date: Nov 30, 2022
Description: Play a game of battleship with the computer
Bugs: No bugs
Plan:
    1)Generate a board for both the player and the computer with four randomly placed ships
    2)Ask the player where they want to shoot
    3)Put a * if they didn't hit a ship and a ! if they did on the computer's board
    4)Computer shoots a random spot
    5)Put a * if they didn't hit a ship and a ! if they did on the players's board
    6)Repeat until there is a winner
"""
import random


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

        if board[r][c] == "X":  # if spot already chosen, try again
            continue
        else:
            board[r][c] = "X"  # put an X in that spot
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


def playerChoice(board2):
    """
    The player's choice of where to shoot
    Arguments:
        board2: the computer's board
    Returns:
        A * on the board if there is no ship in that spot
        A ! on the board if there is a ship in that spot
    """

    r = int(input("Pick a row"))  # row
    c = int(input("Pick a column"))  # column

    if 0 > c > 4 or 0 > r > 4:  # if number smaller than 0 or bigger than 2
        print("Please enter valid numbers")
        playerChoice(board2, board2)

    elif (board2[r][c] == "X"):  # if ship in that spot
        board2[r][c] = "!"
        print("You hit a ship!")

    elif (board2[r][c] == "*") or (board2[r][c] == "!"):  # if spot already taken
        print("Spot already chosen. Choose again")
        playerChoice(board2)

    else:
        board2[r][c] = "*"  # put an X where the player chose

    return board2


def computerChoice(board1):
    """
    Randomize the computer's choice of where to shoot
    Arguments:
        board1: the player's board
    Returns:
        A * on the board if there is no ship in that spot
        A ! on the board if there is a ship in that spot
        """

    r = random.randint(0, 4)  # random r from 0-2
    c = random.randint(0, 4)  # random c from 0-2

    if (board1[r][c] == "X"):  # if ship in that spot
        board1[r][c] = "!"
        print("Computer hit your ship")

    elif (board1[r][c] == "*") or (board1[r][c] == "!"):  # if spot already taken
        playerChoice(board1)
    else:
        board1[r][c] = "*"  # put an * in the spot chosen

    return board1


def winGame(board1, board2):
    """
    Conditions to win the game
    Arguments:
        board1: the player's board
        board2: the computer's board
    Returns:
        Determine if there's a winner
    """

    if (board1[0][0] != "X") and (board1[0][1] != "X") and (board1[0][2] != "X") and (board1[0][3] != "X") and (
            board1[0][4] != "X") and (board1[1][0] != "X") and (board1[1][1] != "X") and (board1[1][2] != "X") and (
            board1[1][3] != "X") and (board1[1][4] != "X") and (board1[2][0] != "X") and (board1[2][1] != "X") and (
            board1[2][2] != "X") and (board1[2][3] != "X") and (board1[2][4] != "X") and (board1[3][0] != "X") and (
            board1[3][1] != "X") and (board1[3][2] != "X") and (board1[3][3] != "X") and (board1[3][4] != "X") and (
            board1[4][0] != "X") and (board1[4][1] != "X") and (board1[4][2] != "X") and (board1[4][3] != "X") and (
            board1[4][4] != "X"):
        print("Computer wins")  # if all the X's are hit on the player's board
        return 1

    elif (board2[0][0] != "X") and (board2[0][1] != "X") and (board2[0][2] != "X") and (board2[0][3] != "X") and (
            board2[0][4] != "X") and (board2[1][0] != "X") and (board2[1][1] != "X") and (board2[1][2] != "X") and (
            board2[1][3] != "X") and (board2[1][4] != "X") and (board2[2][0] != "X") and (board2[2][1] != "X") and (
            board2[2][2] != "X") and (board2[2][3] != "X") and (board2[2][4] != "X") and (board2[3][0] != "X") and (
            board2[3][1] != "X") and (board2[3][2] != "X") and (board2[3][3] != "X") and (board2[3][4] != "X") and (
            board2[4][0] != "X") and (board2[4][1] != "X") and (board2[4][2] != "X") and (board2[4][3] != "X") and (
            board2[4][4] != "X"):
        print("You win!")  # if all the X's are hit on the computer's board
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
    Play a game of Battleship
    Arguments:
        N/A
    Returns:
        N/A
    """

    game = 0

    print("Let's play Battleship!")

    board1 = [["[]", "[]", "[]", "[]", "[]"],
              ["[]", "[]", "[]", "[]", "[]"],
              ["[]", "[]", "[]", "[]", "[]"],
              ["[]", "[]", "[]", "[]", "[]"],
              ["[]", "[]", "[]", "[]", "[]"]]

    board2 = [["[]", "[]", "[]", "[]", "[]"],
              ["[]", "[]", "[]", "[]", "[]"],
              ["[]", "[]", "[]", "[]", "[]"],
              ["[]", "[]", "[]", "[]", "[]"],
              ["[]", "[]", "[]", "[]", "[]"]]

    board1 = startBoard(board1)
    board2 = startBoard(board2)
    printBoard(board1)
    # print("")
    # printBoard(board2)

    while game == 0:
        board2 = playerChoice(board2)
        game = winGame(board1, board2)
        # changeBoard(board2, game)

        board1 = computerChoice(board1)
        game = winGame(board1, board2)
        changeBoard(board1, game)


if __name__ == '__main__':
    main()