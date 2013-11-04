import random  # lets us generate a fake current position
from math import radians, cos, sin, asin, sqrt, fabs


class GPS(object):
    # initialization code
    def __init__(self):
        self.waypoints = dict()
        self.paths = dict()

    # gets current location
    def getLoc(self):
        # as we cannot get the actual location (which would always be the same for a desktop), this is random
        lat = random.random() * 180 - 90
        lon = random.random() * 360 - 180

        wp = Waypoint(lat, lon)
        return (wp)

    # get waypoint and return it
    def getWaypoint(self, waypoint):
        return self.waypoints[waypoint]

    # get waypoints and return them
    def getWaypoints(self):
        return self.waypoints

    # returns path
    def getPath(self, path):
        return self.paths[path]

    # returns paths
    def getPaths(self):
        return self.paths

    # returns number of waypoints
    def waypointsSaved(self):
        return len(self.waypoints.keys())

    # returns number of paths
    def pathsSaved(self):
        return len(self.paths.keys())

    # creates a new path
    def savePath(self, name):
        self.paths[name] = Path()

    # adds point to path, creates both if they do not exist
    def addPoint(self, path, point):
        if not path in self.paths.keys():
            self.savePath(path)

        if not point in self.waypoints.keys():
            self.saveWaypoint(point)

        # add the point to the path
        self.paths[path].addWaypoint(point)

    # removes all instances of a point in given path
    def removePoint(self, path, point):
        if path in self.paths.keys() and point in self.waypoints.keys():
            self.paths[path].removeWaypoint(point)

    # saves the coordinates at a waypoint called the passed name
    def saveWaypoint(self, name):
        self.waypoints[name] = self.getLoc()

    # calculates distance between two points
    def distance(self, point1, point2=None):
        '''Decided to make this return real distance, borrowed code from stackoverflow'''
        point1 = self.getWaypoint(point1)

        if point2 in self.waypoints.keys():
            point2 = self.getWaypoint(point2)
        else:
            point2 = self.getLoc()

        # convert to radians
        lon1, lat1, lon2, lat2 = map(radians,
            [point1.getLon(), point1.getLat(), point2.getLon(), point2.getLat()])

        # haversine formula
        dlon = lon1 - lon2
        dlat = lat1 - lat2
        a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
        c = 2 * asin(sqrt(a))
        return 6367 * c  # kilometers

    # calculates the total distance for a path
    def pathDistance(self, name):
        distance = 0
        if name in self.paths.keys():
            pairs = self.paths[name].getPathPairs()

            for pair in pairs:
                distance += self.distance(pair[0], pair[1])

        return distance

    # replaces default identifier when used as a string
    def __str__(self):
        return '\n====================\n Paths:\t\t{0}\n Waypoints:\t{1}\n===================='.format(self.pathsSaved(), self.waypointsSaved())



class Waypoint(object):
    # initialization code
    def __init__(self, lat=0.0, lon=0.0):
        self.lat = lat
        self.lon = lon

    # returns the waypoint's assigned latitude
    def getLat(self):
        return self.lat

    # returns the waypoint's assigned longitude
    def getLon(self):
        return self.lon

    # replaces default identifier when waypoint used in a string
    def __str__(self):
        return '[{0}, {1}]'.format(self.lat, self.lon)



class Path(list):
    # initialization code
    def __init__(self):
        self.waypoints = list()

    # adds a waypoint to the list
    def addWaypoint(self, wp):
        self.waypoints.append(wp)

    # removes each instance of a waypoint if it is in path
    def removeWaypoint(self, wp):
        self.waypoints = [coord for coord in self.waypoints if coord != wp]

    # returns a lits of the path in pairs
    def getPathPairs(self):
        pairs = list()

        last = None

        for wp in self.waypoints:
            if last != None:
                pairs.append([last, wp])
            last = wp

        return pairs

    # replaces the default identifier when list is used in a string
    def __str__(self):
        return '{0} Waypoints'.format(len(self.waypoints))
