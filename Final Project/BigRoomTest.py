from FinalI import *
from sys import exit

# runs an interface 
def interface(pc):
    disp = 'You are in a big room.'
    disp += pc.wallWarnings()
    disp += pc.checkDirs()
    # display status display
    print(disp)

    # get input
    cmd = input('? ')
    if goodInput(cmd):
        cmd = fullDir(cmd)
        if cmd == 'Quit':
            print('Goodbye!')
            exit()
        else:
            print(pc.move(cmd))
    else:
        print('I do not understand {}.'.format(cmd))
    return pc


# checks input
def goodInput(way):
    way = way.lower()
    validDirs = ['n','s','e','w', 'q', 'north', 'south', 'east', 'west', 'quit']
    return way in validDirs


# gets the full length version of a direction
def fullDir(way):
    way = way.lower()
    dirDict = {'n':'North', 'north':'North',
        's':'South', 'south':'South',
        'e':'East', 'east':'East',
        'w':'West', 'west':'West',
        'q':'Quit', 'quit':'Quit'}
    return dirDict[way]


# main function for big room test
def main():
    # instantiate intances of room and player
    room = Room()
    pc = PC(room)

    while True:
        pc = interface(pc)


# run if this is the file called
if __name__ == '__main__':
    main()
