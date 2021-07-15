import random

## Need to establish which player goes first through randomization
player = input("Please enter your name:")
cpu = "CPU"

p_order = [player,cpu]



if player:
    random.shuffle(p_order)
    if p_order[0] == player:
        print(f"{player} you are Player 1. You go first!")
        print(f"{cpu} is Player 2!")
    elif p_order[0] == cpu:  
        print(f"{cpu} is Player 1. They go first!")
        print(f"{player} your Player 2!")

## Need to draw board

a = [["-","-","-"],["-","-","-"],["-","-","-"]]

for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=" ")
    print()

## Need to assign X or O to each player
    ## Randomize who gets X or O
## Need to start game once Players and turns are established
    ## While loop in game
## Need to assign x and o to area on board player chooses
## CPU chooses randomly
## Game stops when a player gets 3 in a row
## Need to display winner when game is over
## Give score
## Be able to play again
    ## WHile Loop false
## Game ends when the first player reaches 3 points
    ## Increment points and display them
## Be able to start whole game over
    ## Second while loop false