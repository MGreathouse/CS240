# coordinates are not currently important other than meta knowledge as having to be in a negative
# range, so for functionality this will use a 0 minimum value instead and just convert the coordinates
# into the expected values if needed

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

    # returns the center coordinate as two integers
    def getCenter(self):
        return self.center[0], self.center[1]

    # add the character into slot
    def addPC(self, pc):
        w, l = self.getCenter()
        self.floor[w + pc.x][l + pc.y] = pc

    # display variables
    # displays with top left as base: (0,0) in real coords
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


class PC(object):
    # initialization method
    def __init__(self, room, x=0, y=0):
        self.x = x
        self.y = y
        self.room = room
        self.room.addPC(self)

    # display methods
    def __str__(self):
        return 'P'

    def __repr__(self):
        return 'P: [{}, {}]'.format(self.x, self.y)
