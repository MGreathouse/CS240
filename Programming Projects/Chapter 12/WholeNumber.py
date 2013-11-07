class WholeNumber(int):
    # initialization class
    def __init__(self, num=0):
        num = int(num)
        if num < 0:
            ValueError('Whole Numbers must be non-negative!')
        self.value = num

    # addition
    def __add__(self, num2):
        if self.value + num2 < 0:
            ValueError('Whole Numbers must be non-negative!')
        else:
            return int(self.value + num2)

    # subtraction
    def __sub__(self, num2):
        if self.value - num2 < 0:
            ValueError('Whole Numbers must be non-negative!')
        else:
            return int(self.value - num2)

    # multiplication
    def __mul__(self, num2):
        if self.value * num2 < 0:
            ValueError('Whole Numbers must be non-negative!')
        else:
            return int(self.value * num2)

    # division
    def __truediv__(self, num2):  # __div__ is a Python 2.X holdover and is useless in 3.0
        if self.value / num2 < 0:
            ValueError('Whole Numbers must be non-negative!')
        else:
            return int(self.value / num2)

    # floor division
    def __floordiv__(self, num2):
        if self.value // num2 < 0:
            ValueError('Whole Numbers must be non-negative!')
        else:
            return int(self.value // num2)

    # self value
    def __str__(self):
        return(self.value)
