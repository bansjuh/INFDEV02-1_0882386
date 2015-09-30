#-----------------------------------------------------------------------------------------------------
#
# Created by:           Julian Mansveld
# Time Created:         23/10/2015
# Class:                INV1B
# Student Number:       0882386
#
#------------------------------------------------------------------------------------------------------

import random
name = raw_input( " What is your name? \n ")
print " Hello " + name
playerChoice = raw_input(" Choose between Rock, Paper or Scissors \n ").lower() # if caps are used it wil convert it to lower characters.
#random.randint will genarate a random number between 1 and 3 that we will link to a choice of rock,paper or scissors
computerChoice = random.randint(1, 3) # 1 = Rock, 2 = Paper, 3 = Scissors
while (playerChoice != "rock" and playerChoice != "paper" and playerChoice != "scissors"  and playerChoice != "lizard"  and playerChoice != "spock" ):#
    playerChoice = raw_input("I thought we played a game of Rock, Paper, Scissors, Lizard or Spock: ")
if playerChoice == ("rock"):
    if computerChoice == (1):
        print "Rock agianst Rock, Nothing happens. Tie Game."
    elif computerChoice == (2):
        print "To bad, the opponents Paper covered your Rock. You Loose."
    elif computerChoice == (3):
        print "Well done, your Rock crushed the opponents Scissors! You Win."
if playerChoice == ("paper"):
    if computerChoice == (1):
        print "Well done, you covered the Rock with your Paper! You Win."
    elif computerChoice == (2):
        print "Paper agianst Paper, nothing happens. Tie Game."
    elif computerChoice == (3):
        print "To bad, the opponents Scissors cuts your Paper! You Loose."
if playerChoice == ("scissors"):
    if computerChoice == (1):
        print "To bad, the opponents Rock crushed your Scissors! You Loose."
    elif computerChoice == (2):
        print "Well done, your Scissors cuts the opponents Paper! You Win."
    elif computerChoice == (3):
        print "Scissors agianst Scissors, nothing happens. Tie Game."
print "\n Thank you for playing " + name + ". Till next time!"