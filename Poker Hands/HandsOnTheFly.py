#======================================================================================
# Marcus Greathouse
# CS240 Fall 2013
# Poker Hands Program
# ------------------------------------------------------------------------------------
# This program will get from the user whether standard poker rules apply, or texas
# Hold'em rules apply, as well as how many hands will be checked before the hand is
# randomly generated and then checked to see what was generated
#======================================================================================

from random import *
from itertools import *

# card strength dictionary
strengthDict = {0: 'Nothing',
                1: 'One Pair',
                2: 'Two Pairs',
                3: 'Three of a Kind',
                4: 'Straight',
                5: 'Flush',
                6: 'Full House',
                7: 'Four of a Kind',
                8: 'Straight Flush',
                9: 'Royal Flush'}

# helper functions
# converts the cards from number to card format
def toCard(card):
    cardText = ''

    # convert card value
    if card[0] == 1:
        cardText = 'A'
    elif card[0] == 11:
        cardText = 'J'
    elif card[0] == 12:
        cardText = 'Q'
    elif card[0] == 13:
        cardText = 'K'
    else:
        cardText = str(card[0])

    # convert suit
    if card[1] == 0:
        cardText += '\u0003'
    elif card[1] == 1:
        cardText += '\u0004'
    elif card[1] == 2:
        cardText += '\u0005'
    elif card[1] == 3:
        cardText += '\u0006'

    return cardText


# generates a list of all possible 5-card hands
def getHands(hand):
    return list(combinations(hand, 5))


# converts hand strength to a nice string version
def getStrength(strengthInt):
    return strengthDict[strengthInt]


# generate the deck
deck = list()
hand = list()
possibleHands = list()

for i in range(1,14):
    for j in range(4):
        deck.append([i, j])
# get parameters
numHands = 0
while numHands <= 0:
    try:
        numHands = int(input('Number of hands to test: '))
    except:
        print('That is not a valid number. Try again.')

numCards = 0
while numCards <= 0:
    try:
        numCards = int(input('5 or 7 card hand: '))
        if numCards != 5 and numCards != 7:
            numCards = 0
            a = 1 / 0 # forcing an error to be thrown since I am lazy and can use the input try statement
    except:
        print('That is not a valid number. Try again.')

for loop in range(numHands):
    winningHand = list()

    # randomize the deck
    shuffle(deck)

    # get the hand and order it !!!ordering it is important!!!
    hand = deck[0:numCards]
    hand.sort()                 # If this is not done, most checks will fail

    # get all the potential 5 card hands
    possibleHands = [list(elem) for elem in getHands(hand)]

    # check each 5 card hand
    for pHand in possibleHands:
        pHand.sort()
        # check cards for highest hand
        handStrength = 0

        # check if a royal flush
        if handStrength == 0:
            suit = pHand[0][1]
            cardsNeeded = [1, 10, 11, 12, 13]

            if pHand[0][0] == 1:
                cardsNeeded.remove(1)

            for card in pHand[-4:]:
                if cardsNeeded.count(card[0]) != 0:
                    if card[1] == suit:
                        suit = card[1]
                        cardsNeeded.remove(card[0])
                else:           #Not a royal flush
                    break

            #check to see if all reqs were met
            if len(cardsNeeded) == 0:
                handStrength = 9

        # check if a straight flush
        if handStrength == 0:
            suit = pHand[0][1]
            prev = pHand[0][0]
            inARow = 1

            for card in pHand[1:]:
                if (card[0] == prev + 1 or (card[0] == 11 and prev == 1 and pHand[2][1] == 12)) and (card[1] == suit):
                    prev = card[0]
                    inARow += 1
                else:
                    break

            if inARow == 5:
                handStrength = 8

        # check for 4 of a kind
        if handStrength == 0:
            if pHand[0][0] == pHand[3][0] or pHand[1][0] == pHand[4][0]:
                handStrength = 7

        # check for a full house
        if handStrength == 0:
            if (pHand[0][0] == pHand[1][0] and pHand[2][0] == pHand[4][0]) or (pHand[0][0] == pHand[2][0] and pHand[3][0] == pHand[4][0]):
                handStrength = 6

        # check for a flush
        if handStrength == 0:
            if pHand[0][1] == pHand[1][1] and pHand[0][1] == pHand[2][1] and pHand[0][1] == pHand[3][1] and pHand[0][1] == pHand[4][1]:
                handStrength = 5

        # check for a straight
        if handStrength == 0:
            prev = pHand[0][0]
            inARow = 1

            for card in pHand[1:]:
                if card[0] == prev + 1 or (card[0] == 11 and prev == 1 and pHand[2][1] == 12):
                    prev = card[0]
                    inARow += 1
                else:
                    break

            if inARow == 5:
                handStrength = 4

        # check for three of kind
        if handStrength == 0:
            for i in range(3):
                if pHand[i][0] == pHand[i + 1][0] and pHand[i + 1][0] == pHand[i + 2][0]:
                    handStrength = 3

        # check for two pair
        if handStrength == 0:
            # if the hand is a three of a kind, this check will never trigger
            if pHand[0][0] == pHand[1][0]:
                if pHand[2][0] == pHand[3][0]:
                    handStrength = 2
                elif pHand[3][0] == pHand[4][0]:
                    handStrength = 2
            elif  pHand[1][0] == pHand[2][0] and pHand[3][0] == pHand[4][0]:
                handStrength = 2

        # check for a single pair
        if handStrength == 0:
            for i in range(4):
                if pHand[i][0] == pHand[i + 1][0]:
                    handStrength = 1

        # attach the hand strength to the hand
        pHand.append(handStrength)

    # get best hand usig a lambda metod I do not understand, but works
    possibleHands.sort(key = lambda x: x[5])
    winningHand = possibleHands[-1]

    # convert hand to a string
    handString = ''
    for i in range(5):
        handString += ', ' + toCard(winningHand[i])

    handString = handString[2:]
    handStrength = getStrength(winningHand[5])


    print('Hand Value:        ' + handStrength)
    print('Hand:              ' + handString)
    print()
