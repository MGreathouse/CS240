# coordinates are not currently important other than meta knowledge as having to be in a negative
# range, so for functionality this will use a 0 minimum value instead and just convert the coordinates
# into the expected values if needed [keeping track of desired coords in player class]

class Room(object):
    # initialization method
    def __init__(self, width=7, length=7):
        if type(width) == int and type(length) == int:
            # if width or length is even, make it odd 
            if not length % 2:
                length += 1
            if not width % 2:
                width += 1

            floor = []
            
            # rows
            for i in range(length):
                row = []
                # columns
                for j in range(width):
                    row.append(None)
                floor.append(row)

            self.floor = floor
            self.center = [length//2, width//2]
            self.width = width
            self.length = length

    # returns the center coordinate as two integers
    def getCenter(self):
        return self.center[0], self.center[1]

    # add the character into slot - more for debugging
    def addPC(self, pc):
        w, l = self.getCenter()
        self.floor[w + pc.x][l + pc.y] = pc

    # removes player from the room - more for debugging
    def removePC(self, pc):
        w, l = self.getCenter()
        self.floor[w + pc.x][l + pc.y] = None

    # display variables
    # displays with top left as base: (0,0) in real coords (flipped vertically)
    def __str__(self):  # this is mostly for debugging
        string = ''
        for row in self.floor:
            for cell in row:
                if cell:
                    string += '{:<3s}'. format(cell)
                else:
                    string += '.  '
            string += '\n'
        return string


# keeping track of desired coordinates in player
class PC(object):
    # initialization method
    def __init__(self, room, x=0, y=0):
        self.x = x
        self.y = y
        self.room = room
        self.room.addPC(self)

    # check to make sure it is a valid move
    def checkMove(self, way):
        realX, realY = self.room.getCenter()
        realX += self.x
        realY += self.y

        if way[0].lower() == 'n':
            if realX < self.room.length - 1:
                return True
        elif way[0].lower() == 's':
            if realX > 0:
                return True
        elif way[0].lower() == 'e':
            if realY < self.room.width - 1:
                return True
        elif way[0].lower() == 'w':
            if realY > 0:
                return True

        # returns false if those are invalid
        return False

    # moves player
    def move(self, way):
        if self.checkMove(way):
            # remove the player so the map will update to the fact it is missing
            self.room.removePC(self)

            if way[0].lower() == 'n':
                self.x += 1
            elif way[0].lower() == 's':
                self.x -= 1
            elif way[0].lower() == 'e':
                self.y += 1
            elif way[0].lower() == 'w':
                self.y -= 1

            self.room.addPC(self)
            return 'You travel {} for a bit.'.format(way.lower())
        else:
            return 'That way is blocked'

    # display methods
    # string representation of pc
    def __str__(self):
        return 'P'

    # pc repr
    def __repr__(self):
        return 'P: [{}, {}]'.format(self.x, self.y)

    # gets wall warnings
    def wallWarnings(self):
        realX, realY = self.room.getCenter()
        realX += self.x
        realY += self.y

        # build return string
        # adjacent walls
        disp = ''
        if realX == self.room.length - 1:
            disp += '\nYou are standing next to a wall to the north.'
        if realX == 0:
            disp += '\nYou are standing next to a wall to the south.'
        if realY == self.room.width - 1:
            disp += '\nYou are standing next to a wall to the east.'
        if realY == 0:
            disp += '\nYou are standing next to a wall to the west.'

        # nearby walls
        if realX == self.room.length - 2:
            disp += '\nThere is a wall nearby to the north.'
        if realX == 1:
            disp += '\nThere is a wall nearby to the south.'
        if realY == self.room.width - 2:
            disp += '\nThere is a wall nearby to the east.'
        if realY == 1:
            disp += '\nThere is a wall nearby to the west.'

        return disp

    # get available dirs
    def checkDirs(self):
        n = self.checkMove('n')
        e = self.checkMove('e')
        s = self.checkMove('s')
        w = self.checkMove('w')

        disp = '\nObvious directions:'
        if n:
            disp += ' n'
        if s:
            disp += ' s'
        if e:
            disp += ' e'
        if w:
            disp += ' w'

        return disp

