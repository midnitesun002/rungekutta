
from struct import pack, unpack
from math import frexp
from Morton_Naive import *

bits = 4
int_type = "Q"
float_type = "d"
#for i in range(2**4):
for i in [5.342715, 6.4367151, 7.834298]:
	#xb = unpack(">I", pack(">f", i/2**bits))[0]
	xb = unpack(">I", pack(">f", i))[0]
	bstring = ''.join([str((xb >> (31 - k)) & 1) for k in range(32)])
	#print('%f: %s' % (i/2**bits, bstring))
	print('%f: %s' % (i, bstring))

x = 0.456
y = 0.467
print(frexp(x))
print(frexp(y))

z = 0.5
xi = unpack(">I", pack(">f", x))[0]
yi = unpack(">I", pack(">f", y))[0]
zi = unpack(">I", pack(">f", z))[0]
xyzi = (xi^yi)|zi

xyz = unpack(">f", pack(">I", xyzi))[0]
print(xyz)
print(frexp(xyz-z))

print(msdb2(decfrac2man(0.5), decfrac2man(0.315)))