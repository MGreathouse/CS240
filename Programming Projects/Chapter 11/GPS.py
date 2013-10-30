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
        return (lat, lon)

    # get waypoint and return it
    def getWaypoint(self, waypoint):
        return self.waypoints(waypoint)

    # returns number of waypoints
    def waypointsSaved(self):
        return len(self.waypoints.keys())

    # returns number of paths
    def pathsSaved(self):
        return len(self.paths.keys())

    # saves the coordinates at a waypoint called the passed name
    def saveWaypoint(self, name):
        self.waypoints[name] = self.getLoc()

    # calculates distance between two points
    def distance(self, point1, point2=None):
        '''Decided to make this return real distance, borrowed code from stackoverflow'''
        if point2 == None:
            point2 = self.getLoc()
        else:
            point2 = self.waypoints[point2]

        point1 = self.waypoints[point1]

        # convert to radians
        lon1, lat1, lon2, lat2 = map(radians, [point1[1], point1[0], point2[1], point2[0]])

        # haversine formula
        dlon = lon1 - lon2
        dlat = lat1 - lat2
        a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
        c = 2 * asin(sqrt(a))
        return 6367 * c  # kilometers
