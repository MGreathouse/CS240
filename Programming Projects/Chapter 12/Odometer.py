class Odometer(object):
    # initialization method
    def __init__(self, mileage=0.0, dispKilo=False):
        if isinstance(mileage, (int, float)) and type(dispKilo) == bool:
            self.mileage = mileage
            self.dispKilo = dispKilo
        else:
            ValueError('This class only accepts a number and boolean!')

    # converts to kilometers
    def toKilo(self, miles):
        return miles * 1.60934

    # switch miles/kilometers
    def toggleUnit(self):
        self.dispKilo = not self.dispKilo

    # returns the mileage - converts to kilometers if set
    def getMileage(self):
        mileage = self.mileage
        # conver to kilos if appropriate
        if self.dispKilo:
            mileage = self.toKilo(mileage)
        return mileage

    # display
    def __str__(self):
        mileage = self.getMileage()
        return str(round(mileage, 1))

    # went with the full value, figured more identifying than __str__
    def __repr__(self):
        return str(self.getMileage())

    # addition
    def __add__(self, num):
        if isinstance(num, (int, float)):
            return self.getMileage() + num
        else:
            ValueError('Invalid format added to Odometer value, use a number!')

    # subtraction
    def __sub__(self, num):
        if isinstance(num, (int, float)):
            return self.getMileage() - num
        else:
            ValueError('Invalid format subtracted from Odometer value, use a number!')
