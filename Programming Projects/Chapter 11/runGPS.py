from sys import exit
import GPS

# display basic stats about GPS unit
def displayStatus(myGPS):
    print('\nPaths:\t\t{0}\nWaypoints:\t{1}'.format(myGPS.pathsSaved(), myGPS.waypointsSaved()))


# runs interface
def gpsUI(myGPS):
    print('\nCommands:')
    print('Save:\t\t\'s\'')
    print('Path:\t\t\'p\'')
    print('Distance:\t\'d\'')
    print('Quit:\t\t\'q\'\n')

    # get command
    cmd = input('Enter Command: ')

    if cmd == 'q':
        exit()  # self explanatory
    elif cmd == 's':
        # save current location
        name = input('Waypoint Name: ')
        myGPS.saveWaypoint(name)
        print('\n{0} saved as Waypoint \'{1}\''.format(myGPS.waypoints[name], name))
    elif cmd == 'd':
        toPoint = input('\nWaypoint: ')
        try:
            distance = myGPS.distance(toPoint)
            print('Waypoint {0} is {1} kilometers away.'.format(toPoint, distance))
        except:
            print('\nInvalid Waypoint!')

    # return the gps for the next loop
    return(myGPS)


# runs if this file is run directly
def runGPS():
    gipped = GPS.GPS()

    while True:  # not as bad as it looks, can be killed in interface
        #display current status
        displayStatus(gipped)

        #run through one iteration of user input
        gipped = gpsUI(gipped)


if __name__ == '__main__':
    runGPS()
