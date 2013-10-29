import random  # lets us generate a fake current position
import math


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
        if point2 == None:
            point2 = self.getLoc()

        n = self.waypoints[point1][0] - self.waypoints[point2][0]
        d = self.waypoints[point1][1] - self.waypoints[point2][1]

        return math.fabs(n / d)
