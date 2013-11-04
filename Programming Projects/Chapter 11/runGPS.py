from sys import exit
import GPS


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
    elif cmd == 'p':
        # opens path menu
        print('\nPaths:')
        # start a new inner loop that will run until a path command is executed
        while True:  # breaks out itself
            print('\nPath Commands:')
            print('New:\t\t\'n\'')
            print('Add Point:\t\'a\'')
            print('Remove Point:\t\'r\'')
            print('Distance:\t\'d\'')
            print('Cancel\t\t\'c\'\n')
            cmd = input('Enter Command: ')

            if cmd == 'c':
                break
            elif cmd == 'n':
                # create a new path
                path = input('Path Name: ')
                myGPS.savePath(path)
                break
            elif cmd == 'a':
                # adds a point to a path
                print('\nPaths:')
                for pt in myGPS.getPaths():
                    print(pt)

                path = input('\nPath Name: ')
                name = input('Waypoint Name: ')
                # adds waypoint to the path, creates both if neither exists
                myGPS.addPoint(path, name)
                break
            elif cmd == 'r':
                # removes all instances of a point in a path
                print('\nPaths:')
                for pt in myGPS.getPaths():
                    print(pt)

                path = input('\nPath Name: ')
                name = input('Waypoint Name: ')
                # adds waypoint to the path, creates both if neither exists
                myGPS.removePoint(path, name)
                break;
            elif cmd == 'd':
                # get total distance of path
                print('\nPaths:')
                for pt in myGPS.getPaths():
                    print(pt)
                name = input('\nPath Name: ')
                distance = myGPS.pathDistance(name)
                print('Path {0} is {1} kilometers long.'.format(name, distance))
                break


    elif cmd == 'd':
        # calculates distance from current location to given point
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
        print(gipped)

        #run through one iteration of user input
        gipped = gpsUI(gipped)


if __name__ == '__main__':
    runGPS()
