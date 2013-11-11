class Compass(object):
    def __init__(self, degrees=0, minutes=0):
        # make sure valid values
        if type(degrees) == int and type(minutes) == int:
            self.degrees = degrees
            self.minutes = minutes
            self.degrees, self.minutes = self.reduce(self.degrees, self.minutes)
        else:
            ValueError('Invalid Number: Degrees and minutes are both integers.')

    # reduces the values passed in and returns them as proper values
    def reduce(self, degrees, minutes):
        # take care of negative values
        while minutes < 0:
            minutes += 60
        while degrees < 0:
            degrees += 360

        # take care of overly large numbers
        while minutes > 59:
            minutes -= 60
            degrees += 1
        while degrees > 359:
            degrees -= 360

        return degrees, minutes

    # display methods
    def __str__(self):
        return '{:>4} degree(s), {:>3} minute(s)'.format(self.degrees, self.minutes)

    def __repr__(self):
        return self.__str__()

    # addition
    def __add__(self, num):
        # check num type
        if type(num) == int:
            return '{:>4} degree(s), {:>3} minute(s)'.format(*self.reduce(self.degrees + num, self.minutes))
        elif type(num) == Compass:
            return '{:>4} degree(s), {:>3} minute(s)'.format(*self.reduce(self.degrees + num.degrees, self.minutes + num.minutes))
