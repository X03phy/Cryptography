from Crypto.Util.number import *
import gmpy2

g = 209
p = 991
d = inverse(g, p)

print(d)