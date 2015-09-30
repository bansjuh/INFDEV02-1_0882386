#-----------------------------------------------------------------------------------------------------
#
# Created by:           Julian Mansveld
# Time Created:         23/10/2015
# Class:                INV1B
# Student Number:       0882386
#
#------------------------------------------------------------------------------------------------------

import random
name = raw_input(" What is your name? \n ")
print " Hello " + name 

playerChoice = raw_input(" Choose between Rock, Paper, Scissors, Lizard or Spock \n ").lower() # if caps are used it wil convert it to lower characters.
#random.randint will genarate a random number between 1 and 3 that we will link to a choice of rock,paper or scissors
computerChoice = random.randint(1, 5) # 1 = Rock, 2 = Paper, 3 = Scissors, 4 = Lizard, 5 = spock
while (playerChoice != "rock" and playerChoice != "paper" and playerChoice != "scissors"  and playerChoice != "lizard"  and playerChoice != "spock" ):#
    playerChoice = raw_input("I thought we played a game of Rock, Paper, Scissors, Lizard or Spock: ")
if playerChoice == ("rock"):
    if computerChoice == (1):
        print "Rock agianst Rock, Nothing happens. Tie Game."
    elif computerChoice == (2):
        print "Too bad, the opponents Paper covered your Rock. You Loose."
    elif computerChoice == (3):
        print "Well done, your Rock crushed the opponents Scissors! You Win."
    elif computerChoice == (4):
        print "Well done, your Rock crushed the opponents Lizard! You Win."
    elif computerChoice == (5):
        print "Too bad, the opponents Spock vaporized your Rock. You Loose."
if playerChoice == ("paper"):
    if computerChoice == (1):
        print "Well done, you covered the Rock with your Paper! You Win."
    elif computerChoice == (2):
        print "Paper agianst Paper, nothing happens. Tie Game."
    elif computerChoice == (3):
        print "Too bad, the opponents Scissors cuts your Paper! You Loose."
    elif computerChoice == (4):
        print "Too bad, the opponents Lizard eats your Paper! You Loose."
    elif computerChoice == (5):
        print "Well done, you disproved Spock with your Paper! You Win."
if playerChoice == ("scissors"):
    if computerChoice == (1):
        print "Too bad, the opponents Rock crushed your Scissors! You Loose."
    elif computerChoice == (2):
        print "Well done, your Scissors cuts the opponents Paper! You Win."
    elif computerChoice == (3):
        print "Scissors agianst Scissors, nothing happens. Tie Game."
    elif computerChoice == (4):
        print "Well done, your Scissors decapetates the opponents Lizard! You Win."
    elif computerChoice == (5):
        print "Too bad, the opponents Spock Smashed your Scissors! You Loose."
if playerChoice == ("lizard"):
    if computerChoice == (1):
        print "Too bad, the opponents Rock crushed your Lizard! You Loose."
    elif computerChoice == (2):
        print "Well done, your Lizard eats the opponents Paper! You Win."
    elif computerChoice == (3):
        print "Too bad, your Lizard got decapetated by the opponents Scissors! You Loose."
    elif computerChoice == (4):
        print "Lizard agianst Lizard, Nothing happens. Tie Game."
    elif computerChoice == (5):
        print "Well done, your Lizard posioned the opponents Spock! You Win."
if playerChoice == ("spock"):
    if computerChoice == (1):
        print "Well done, your Spock vaporized the opponents Rock! You Win."
    elif computerChoice == (2):
        print "Too bad, your Spock got disproved by the opponents Paper! You Loose."
    elif computerChoice == (3):
        print "Well done, your Spock Smashed the opponents Scissors! You Win."
    elif computerChoice == (4):
        print "Too bad, your Spock got posioned by the opponents Lizard! You Loose."
    elif computerChoice == (5):
        print "Spock agianst Spock, nothing happens! Tie Game."

print "\n Thank you for playing " + name + ". Till next time!"