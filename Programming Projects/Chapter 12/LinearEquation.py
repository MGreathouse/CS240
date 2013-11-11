class LinearEquation(object):
    # initialization method
    def __init__(self, m=1, b=0):  # defaults to 'y = x'
        if isinstance(m, (int, float)) and isinstance(b, (int, float)):
            self.m = m
            self.b = b
        else:
            ValueError('Values passed must be numbers!')

    # getters
    # get m
    def m(self):
        return self.m

    # get b
    def b(self):
        return self.b

    # returns the value for the equation at given point
    def value(self, x):
        if isinstance(x,(int, float)):
            result = self.b
            result += self.m * x
            return result
        else:
            ValueError('Value passed must be a number!')

    # composes two function *[f(g(x))]
    def compose(self, gofx):
        if type(gofx) == LinearEquation:
            new_m = self.m * gofx.m
            new_b = self.m * gofx.b + self.b
            return LinearEquation(new_m, new_b)
        else:
            ValueError('Value passed in must be a Linear Equation!')

    # display methods
    def __str__(self):
        return 'y = {0}x + {1}'.format(self.m, self.b)

    # might as well be the same as str, no significant way to otherwise do it
    def __repr__(self):
       return self.__str__()

    # addition
    def __add__(self, gofx):
        if type(gofx) == LinearEquation:
            new_m = self.m + gofx.m
            new_b = gofx.b + self.b
            return LinearEquation(new_m, new_b)
        else:
            ValueError('Value added must be a Linear Equation!')
