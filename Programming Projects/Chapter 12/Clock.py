import re

# this is a 12 hour clock
class Clock(object):
    # initialization method
    def __init__(self, time=False):  # midnight default
        if not time:
            time = 0
        self.initTime(time)

    # tries to get and set the time based on input
    def initTime(self, time):
        format = type(time)
        if format == int:
            # this is good, straightup conversion to HH:MM:SS
            self.hours = time // 3600
            time = max(time - self.hours * 3600, 0)
            self.minutes = time // 60
            time = max(time - self.minutes * 60, 0)
            self.seconds = time
        elif format == str:
            # this is not so good - need to convert
            triggerError = True

            pattern = re.compile('[0-9][0-9][:][0-9][0-9][:][0-9][0-9][a-zA-Z0-9_][a-zA-Z0-9_][a-zA-Z0-9_]')
            results = pattern.match(time)
            if results:
                splitter = time.split(':')
                self.hours = int(splitter[0])
                self.minutes = int(splitter[1])
                self.seconds = int(splitter[2][0:2])
                triggerError = False

            pattern = re.compile('[0-9][0-9][:][0-9][0-9][:][0-9][0-9][a-zA-Z0-9_][a-zA-Z0-9_]')
            results = pattern.match(time)
            if results:
                splitter = time.split(':')
                self.hours = int(splitter[0])
                self.minutes = int(splitter[1])
                self.seconds = int(splitter[2][0:2])
                triggerError = False

            pattern = re.compile('[0-9][0-9][:][0-9][0-9][:][0-9][0-9]')
            results = pattern.match(time)
            if results:
                splitter = time.split(':')
                self.hours = int(splitter[0])
                self.minutes = int(splitter[1])
                self.seconds = int(splitter[2])
                triggerError = False

            pattern = re.compile('[0-9][0-9][:][0-9][0-9]')
            results = pattern.match(time)
            if results:
                splitter = time.split(':')
                self.hours = int(splitter[0])
                self.minutes = int(splitter[1])
                self.seconds = 0
                triggerError = False

            pattern = re.compile('[0-9][:][0-9][0-9][:][0-9][0-9][a-zA-Z0-9_][a-zA-Z0-9_][a-zA-Z0-9_]')
            results = pattern.match(time)
            if results:
                splitter = time.split(':')
                self.hours = int(splitter[0])
                self.minutes = int(splitter[1])
                self.seconds = int(splitter[2][0:2])
                triggerError = False

            pattern = re.compile('[0-9][:][0-9][0-9][:][0-9][0-9][a-zA-Z0-9_][a-zA-Z0-9_]')
            results = pattern.match(time)
            if results:
                splitter = time.split(':')
                self.hours = int(splitter[0])
                self.minutes = int(splitter[1])
                self.seconds = int(splitter[2][0:2])
                triggerError = False

            pattern = re.compile('[0-9][:][0-9][0-9][:][0-9][0-9]')
            results = pattern.match(time)
            if results:
                splitter = time.split(':')
                self.hours = int(splitter[0])
                self.minutes = int(splitter[1])
                self.seconds = int(splitter[2])
                triggerError = False

            pattern = re.compile('[0-9][:][0-9][0-9]')
            results = pattern.match(time)
            if results:
                splitter = time.split(':')
                self.hours = int(splitter[0])
                self.minutes = int(splitter[1])
                self.seconds = 0
                triggerError = False

            if triggerError:
                ValueError('Invalid Time: Either input seconds or time as a string.')

        if not self.hours:
            ValueError('Invalid Time: Either input seconds or time as a string.')

        while self.hours > 11:
            self.hours -= 12  # going with a 12 hour clock

    # display string
    def __str__(self):
        return '{:02}:{:02}:{:02}'.format(self.hours, self.minutes, self.seconds)

    # make the repr the same, because why not
    def __repr__(self):
        return self.__str__()

    # addition - ignoring book instructions for adding two times together ~ doing it all
    def __add__(self, num):
        if type(num) == Clock:
            cSum = self.hours + num.hours
            cMin = self.minutes + num.minutes
            cSec = self.seconds + num.seconds
            # convert down to acceptable numbers
            while cSec > 59:
                cSec -= 60
                cMin += 1
            while cMin > 59:
                cMin -= 60
                cSum += 1
            while cSum > 11:
                cSum -= 12
            return '{:02}:{:02}:{:02}'.format(cSum, cMin, cSec)
        elif isinstance(num, (int)):
            cSum = self.hours + num
            while cSum > 11:
                cSum -= 12
            return '{:02}:{:02}:{:02}'.format(cSum, self.minutes, self.seconds)
        else:
            ValueError('Clocks can only be added to integers or other clocks.')
