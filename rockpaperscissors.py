'''
Name: Ellie Hochberg
Date: April 30, 2022
Description: A program to play rock paper scissors single player or multiplayer
Bugs: No bugs that I know of...
Features: 1)Option to play again, 2)keeps score, 3)option to play multiplayer or single player, 4)game determines who wins
Log: Submitted for grading on April 28, 2022
Plan:
    Step 1: Choose whether you want to play single player or multiplayer
    Step 2: If single player, choose rock, paper, or scissors, computer's choice is generated randomly
            If multiplayer, player 1 chooses rock, paper, or scissors first and then player 2 chooses rock, paper, or scissors
    Step 3: Score is displayed
    Step 4: Decide if you want to play again
            If you choose yes, go back to step 1
            If you choose no, game over

Created on Apr 4, 2022

@author: EHochberg23
'''

import random


def main():
    your_score = 0  # variable for your score in single player
    comp_score = 0  # variable for computer score in single player
    p1_score = 0  # variable for player 1 score in multi player
    p2_score = 0  # variable for player 2 score in multi player

    game = True
    while game == True:

        print("1 = single player and 2 = multiplayer\n")
        try:
            pnums = int(input(
                "Do you want to play single player or multiplayer?"))  # choice to play single player or multiplayer
        except:
            print("Error. Enter 1 or 2")
            continue

        if pnums == 1:  # chose to play single player
            print("You chose to play single player\n")
            single = True

            '''
            below is the code to play singleplayer
            you have the option to choose rock, paper or scissors   
            computer's choice is generated randomly
            if you win, your score goes up by one
            if the computer wins, the computer's score goes up by one
            no one gets points if there is a tie
            '''

            print("1 = rock")
            print("2 = paper")
            print("3 = scissors\n")
            while single == True:
                try:
                    player = int(input("Choose one: \n"))  # player's choice
                    computer = random.randint(1, 3)  # computer generates random choice 1, 2, or 3
                    print("You chose", player)
                    print("Computer chose", computer, "\n")

                    if player == 1 and computer == 1:  # both chose rock
                        print("Tie")

                    elif player == 1 and computer == 2:  # player chose rock, computer chose paper
                        print("You lose :(")
                        comp_score = int(comp_score) + 1

                    elif player == 1 and computer == 3:  # player chose rock, computer chose scissors
                        print("You win!!")
                        your_score = int(your_score) + 1

                    elif player == 2 and computer == 1:  # player chose paper, computer chose rock
                        print("You win!!")
                        your_score = int(your_score) + 1

                    elif player == 2 and computer == 2:  # both chose paper
                        print("Tie")

                    elif player == 2 and computer == 3:  # player chose paper, computer chose scissors
                        print("You lose :(")
                        comp_score = int(comp_score) + 1

                    elif player == 3 and computer == 1:  # player chose scissors, computer chose rock
                        print("You lose :(")
                        comp_score = int(comp_score) + 1

                    elif player == 3 and computer == 2:  # player chose scissors, computer chose paper
                        print("You win!!")
                        your_score = int(your_score) + 1

                    elif player == 3 and computer == 3:  # both chose scissors
                        print("Tie")

                    else:
                        print("Error, input 1, 2, or 3")  # invalid input from player
                        continue

                except:
                    print("Error, input 1, 2, or 3")
                    continue

                '''
                below:
                gives the option to play again
                '''

                go = True
                while go == True:
                    print("Computer points:", comp_score)  # prints computer score
                    print("Your points:", your_score, "\n")  # prints your score
                    print("Yes = 1 and No = 2\n")

                    try:
                        choice = int(input("Play again?\n"))  # player's choice to play again or not

                    except:
                        print("Error. Enter 1 or 2")
                        continue

                    if choice == 1:  # player chose to play again
                        game = True
                        go = False
                        single = False
                        continue

                    elif choice == 2:  # player chose to not play again
                        go = False
                        game = False
                        single = False
                        print("Okay, goodbye")
                        break

                    else:
                        print("Error, input 1 or 2")  # invalid input from player


        elif pnums == 2:  # chose to play multiplayer
            print("You chose to play multiplayer\n")
            multi = True
            '''
            below is the code to play multiplayer
            player 1 is given the option to choose rock, paper or scissors   
            player 2 is given the option to choose rock, paper or scissors   
            if player 1 wins, their score goes up by one
            if player 2 wins, their computer's score goes up by one
            no one gets points when there is a tie
            '''

            print("1 = rock")
            print("2 = paper")
            print("3 = scissors\n")

            while multi == True:
                try:
                    p1 = True
                    while p1 == True:
                        try:
                            player1 = int(input("Player 1, choose one: "))  # player 1's choice
                            p1 = False
                            if player1 == 1 or player1 == 2 or player1 == 3:
                                game1 = True
                                p1 = False

                            else:
                                print("Error. Input 1, 2, or 3")  # invalid input from player 1
                                multi = False
                                p1 = True

                        except:
                            print("Error. Input 1, 2, or 3")
                            continue

                    p2 = True
                    while p2 == True:
                        try:
                            player2 = int(input("Player 2, choose one: \n"))  # player 2's choice
                            p2 = False
                            if player2 == 1 or player2 == 2 or player2 == 3:
                                game2 = True
                                p2 = False
                            else:
                                print("Error. Input 1, 2, or 3")  # invalid input from player 2
                                multi = False
                                p2 = True


                        except:
                            print("Error. Input 1, 2, or 3")
                            continue

                    if game1 == True and game2 == True:

                        print("PLayer 1 chose:", player1)
                        print("Player 2 chose:", player2, "\n")

                        if player1 == 1 and player2 == 1:  # both chose rock
                            print("Tie")

                        elif player1 == 1 and player2 == 2:  # player 1 chose rock, player 2 chose paper
                            print("Player 2 wins!")
                            p2_score = int(p2_score) + 1

                        elif player1 == 1 and player2 == 3:  # player 1 chose rock, player 2 chose scissors
                            print("Player 1 wins!")
                            p1_score = int(p1_score) + 1

                        elif player1 == 2 and player2 == 1:  # player 1 chose paper, player 2 chose rock
                            print("Player 1 wins!")
                            p1_score = int(p1_score) + 1

                        elif player1 == 2 and player2 == 2:  # both chose paper
                            print("Tie")

                        elif player1 == 2 and player2 == 3:  # player 1 chose paper, player 2 chose scissors
                            print("Player 2 wins!")
                            p2_score = int(p2_score) + 1

                        elif player1 == 3 and player2 == 1:  # player 1 chose scissors, player 2 chose rock
                            print("Player 2 wins!")
                            p2_score = int(p2_score) + 1

                        elif player1 == 3 and player2 == 2:  # player 1 chose scissors, player 2 chose paper
                            print("PLayer 1 wins!")
                            p1_score = int(p1_score) + 1

                        elif player1 == 3 and player2 == 3:  # both chose scissors
                            print("Tie")

                        else:
                            print("Error, input 1, 2, or 3")  # invalid input
                            continue

                except:
                    print("Error, input 1, 2, or 3")
                    continue

                '''
                below:
                gives the option to play again
                '''

                multigo = True
                while multigo == True:
                    print("Player 2 points:", p2_score)  # prints player 2 score
                    print("Player 1 points:", p1_score, "\n")  # prints player 1 score
                    print("Yes = 1 and No = 2\n")

                    try:
                        choice = int(input("Play again?\n"))  # choice to play again or not

                    except:
                        print("Error. Enter 1 or 2")  # invalid input
                        continue

                    if choice == 1:  # chose to play again
                        game = True
                        multigo = False
                        multi = False
                        continue

                    elif choice == 2:  # chose to not play again
                        multigo = False
                        game = False
                        multi = False
                        print("Okay, goodbye")
                        break


                    else:
                        print("Error, input 1 or 2")


if __name__ == '__main__':
    main()
