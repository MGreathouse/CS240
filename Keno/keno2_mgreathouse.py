#======================================================================================
# Marcus Greathouse
# CS 240 Keno Assignment
#-------------------------------------------------------------------------------------
# Runs a simulation to see the rough odds of winning at each spots level
#======================================================================================

from random import sample

# number of spots to be tested along with each less than itself
spots = 10
# number of tests to do for each spot
tests = 1000000
# number between each report
reportRate = tests

# set the pool
pool = range(1,81)

# get house picks (out of 20)
housePicks = sample(pool, 20)

#set the summary var
summary = list()

winningCombos = {1: ((1, 2.5), ),
                 2: ((2, 10), ),
                 3: ((2, 2), (3, 23)),
                 4: ((2, 1), (3, 5), (4, 65)),
                 5: ((3, 3), (4, 10), (5, 400)),
                 6: ((3, 1), (4, 5), (5, 53), (6, 1500)),
                 7: ((0, 1), (4, 2), (5, 20), (6, 50), (7, 5000)),
                 8: ((0, 2), (4, 1), (5, 7), (6, 50), (7, 500), (8, 10000)),
                 9: ((0, 2), (4, 1), (5, 5), (6, 15), (7, 100), (8, 2000), (9, 20000)),
                 10: ((0, 5), (5, 2), (6, 10), (7, 46), (8, 500), (9, 5000), (10, 100000))}

# investment variables
bestPayout = (None, None)
spotReturn = {}

# helper functions
# displays a report of passed counters
def report(test, counters):
    reportString = ''
    pickList = list(counters.keys())
    pickList.sort()

    totalWins = 0

    # track the average payout
    averagePayout = 0

    for i in winningCombos[spots]:
        if i[0] or i[0] == 0:
            # figure out stats
            totalWins += counters[i[0]]
            percentage = round(counters[i[0]] / test * 100, 2)
            try:
                odds = round(test / counters[i[0]], 2)
            except:
                odds = 0
            # to try can be ass accurate as possible, rounding after it is used in math
            percentage = round(percentage, 3)

            if odds == 0:
                odds = 'N/A'

            # add info to the start of the report list
            reportString = ' ({0})\t\t{1} [{2}%]\t1:{3}\n'.format(i[0], counters[i[0]], round(percentage, 2), odds) + reportString

            # track best return
            payout = i[1] * counters[i[0]]

            averagePayout += payout

    # add total stuff to the end
    percentage = round(totalWins / test * 100, 2)
    try:
        odds = round(test / totalWins, 2)
    except:
        odds = 0
    reportString += ' (Combined)\t{0} [{1}%]\t1:{2}'.format(totalWins, percentage, odds)
    if test == tests:
        summary.append(reportString)

    print('{1}'.format(test, reportString))

    # payout stuff
    averagePayout = round((averagePayout - test), 2)
    spotReturn[spots] = averagePayout

    # for best choice at end
    global bestPayout
    if bestPayout[1] == None or bestPayout[1] < averagePayout:
        bestPayout = (spots, averagePayout)

    print('\nFor {0} tests, the average payout per game would be ${1}'.format(test, round(averagePayout / test, 2)))


# starting at 10 and working down - loop for spots
while spots > 0:
    print()
    print(str(spots) + '-Spot Game\n (Match)\tMatches [%]\tOdds')
    test = 0

    # set up the counters for the spot
    counters = dict()
    for i in range(spots + 1):
        counters[i] = 0

    # loop for number of tests in the spot
    while test < tests:
        # match counter and
        matches = 0

        # get player picks
        picks = sample(pool, spots)

        # check to see picks in house picks
        for pick in picks:
            if pick in housePicks:
                matches += 1

        # after count is figured add the result to the
        if matches in winningCombos.keys() or matches == 0:
            counters[matches] += 1

        # set counter to go to next test
        test += 1

        # check if this is a reporting test
        if test % reportRate == 0:
            report(test, counters)

    # remove a spot for the next round
    spots -= 1

#display a final summary
#for i in range(len(summary)):
#    print('\n{0}:\t{1}'.format(len(summary) - i, summary[i]))

# display overall payout information
print('\nThe best result would be to play {0} spots,\nwhere you will win ${1} over {2} games,\nor about ${3} a game.'.format(
            bestPayout[0], bestPayout[1], tests, round(bestPayout[1] / tests, 2)))
