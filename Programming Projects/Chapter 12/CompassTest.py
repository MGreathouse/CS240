from Compass import *

c = Compass()
print(c)

c = Compass(191, 42)
print(c)

c2 = Compass(359, 61)
print(c2)

print('{}     + {}\n = {}'.format(c, c2, c + c2))
print('{}     + {}\n = {}'.format(725, c2, c2 + 725))
