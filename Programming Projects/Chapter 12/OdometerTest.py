from Odometer import *

newO = Odometer()
oldO = Odometer(1500.1245)

print("New:\t{}\nOld:\t{}".format(newO, oldO))

print('\nNew + 15:\t{}\n'.format(newO + 15))

print('Old (mi):\t{}'.format(oldO))

oldO.toggleUnit()

print('Old (km):\t{}'.format(oldO))
