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

# generate the deck
deck = list()
hand = list()

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

numCards = 5

for loop in range(numHands):
    # randomize the deck
    shuffle(deck)

    # get the hand and order it !!!ordering it is important!!!
    hand = deck[0:numCards]
    hand.sort()                 # If this is not done, most checks will fail

    # check cards for highest hand
    handStrength = 'Nothing'

    # check if a royal flush
    if handStrength == 'Nothing':
        suit = hand[0][1]
        cardsNeeded = [1, 10, 11, 12, 13]

        if hand[0][0] == 1:
            cardsNeeded.remove(1)

        for card in hand[-4:]:
            if cardsNeeded.count(card[0]) != 0:
                if card[1] == suit:
                    suit = card[1]
                    cardsNeeded.remove(card[0])
            else:           #Not a royal flush
                break

        #check to see if all reqs were met
        if len(cardsNeeded) == 0:
            handStrength = 'Royal Flush'

    # check if a straight flush
    if handStrength == 'Nothing':
        suit = hand[0][1]
        prev = hand[0][0]
        inARow = 1

        for card in hand[1:]:
            if (card[0] == prev + 1 or (card[0] == 11 and card[0] != prev)) and (card[1] == suit):
                prev = card[0]
                inARow += 1
            else:
                break

        if inARow == 5:
            handStrength = 'Straight Flush'

    # check for 4 of a kind
    if handStrength == 'Nothing':
        if hand[0][0] == hand[3][0] or hand[1][0] == hand[4][0]:
            handStrength = 'Four of a Kind'

    # check for a full house
    if handStrength == 'Nothing':
        if (hand[0][0] == hand[1][0] and hand[2][0] == hand[4][0]) or (hand[0][0] == hand[2][0] and hand[3][0] == hand[4][0]):
            handStrength = 'Full House'

    # check for a flush
    if handStrength == 'Nothing':
        if hand[0][1] == hand[1][1] and hand[2][1] == hand[3][1] and hand[0][1] == hand[2][1] and hand[0][1] == hand[4][1]:
            handStrength = 'Flush'

    # check for a straight
    if handStrength == 'Nothing':
        prev = hand[0][0]
        inARow = 1

        for card in hand[1:]:
            if card[0] == prev + 1 or (card[0] == 11 and card[0] != prev):
                prev = card[0]
                inARow += 1
            else:
                break

        if inARow == 5:
            handStrength = 'Straight'

    # check for three of kind
    if handStrength == 'Nothing':
        for i in range(3):
            if hand[i][0] == hand[i + 1][0] and hand[i + 1][0] == hand[i + 2][0]:
                handStrength = 'Three of a Kind'

    # check for two pair
    if handStrength == 'Nothing':
        # if the hand is a three of a kind, thi check will never trigger
        if hand[0][0] == hand[1][0]:
            if hand[2][0] == hand[3][0]:
                handStrength = 'Two Pair'
            elif hand[3][0] == hand[4][0]:
                handStrength = 'Two Pair'
        elif  hand[1][0] == hand[2][0] and hand[3][0] == hand[4][0]:
            handStrength = 'Two Pair'

    # check for a single pair
    if handStrength == 'Nothing':
        for i in range(4):
            if hand[i][0] == hand[i + 1][0]:
                handStrength = 'One Pair'


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


    # convert hand to a string
    handString = ''
    for i in range(5):
        handString += ', ' + toCard(hand[i])

    handString = handString[2:]


    print('Hand Value:        ' + handStrength)
    print('Hand:              ' + handString)
    print()
