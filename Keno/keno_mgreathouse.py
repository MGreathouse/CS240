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
reportRate = 100000

# set the pool
pool = range(1,81)

# get house picks (out of 20)
housePicks = sample(pool, 20)

#set the summary var
summary = list()


# helper functions
# displays a report of passed counters
def report(test, counters):
    reportString = ''
    pickList = list(counters.keys())
    pickList.sort()

    totalWins = 0

    for i in pickList:
        if i != 0:
            # figure out stats
            totalWins += counters[i]
            percentage = counters[i] / test
            odds = round(test * percentage, 2)
            # to try can be ass accurate as possible, rounding after it is used in math
            percentage = round(percentage, 3)

            if odds == 0:
                odds = 'N/A'

            # add info to the start of the report list
            reportString = ' ({0}){1}[{2}%]{3}'.format(i, counters[i], percentage, odds) + reportString

    # add total stuff to the end
    percentage = round(totalWins / test, 3)
    odds = round(test * percentage, 2)
    reportString += ' (All){0}[{1}%]{2}'.format(totalWins, percentage, odds)
    if test == tests:
        summary.append(reportString)

    print('{0}:\t{1}'.format(test, reportString))


# starting at 10 and working down - loop for spots
while spots > 0:
    print()
    print(str(spots) + '-Spot Game (Spots Matched)Matches[Percentage]Odds')
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
        counters[matches] += 1

        # set counter to go to next test
        test += 1

        # check if this is a reporting test
        if test % reportRate == 0:
            report(test, counters)

    # remove a spot for the next round
    spots -= 1

#display a final summary
print('\nSUMMARY:\n========')
for i in range(len(summary)):
    print('{0}:\t{1}'.format(len(summary) - i, summary[i]))
