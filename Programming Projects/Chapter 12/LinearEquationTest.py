from LinearEquation import *

f = LinearEquation(2,4)
g = LinearEquation(3,5)
fog = f.compose(g)
gof = g.compose(f)
z = f + g

print('f:\t{}\ng:\t{}\nfog:\t{}\ngof:\t{}\nf+g:\t{}'.format(f, g, fog, gof, z))
