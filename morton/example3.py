
from Morton_Naive import *
from struct import pack, unpack

number = 23.47
print(fman(number))
print(fexp(number))

x = pack(">f", MortonFloat((5.342715, 6.4367151, 7.834298)).code)
print(x)