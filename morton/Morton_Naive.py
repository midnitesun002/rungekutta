
from decimal import Decimal
from functools import reduce
from struct import pack, unpack
from math import frexp

class MortonNaive:
	def __init__(self, pp, bits):
		self.p = pp
		self.bits = bits
		self.dim = len(pp)
		self.computeCode()

	def computeCode(self):
		self.code = 0
		for b in range(self.bits):
			ibits = reduce((lambda x, y: x | y), [((self.p[i] >> (self.bits - 1 - b)) & 1) << i for i in range(self.dim)])
			self.code = (self.code << self.dim) | ibits
			#self.code = (self.code << 2) | ((self.p[0] >> (self.bits - 1 - b)) & 1 ) << 0 | ((self.p[1] >> (self.bits - 1 - b)) & 1 ) << 1

	def __lt__(self, other):
		return self.code < other.code

	def __repr__(self):
		return str((self.p[0], self.p[1]))

	def __getitem__(self, idx):
		return self.p[idx]

class MortonQuick:
	def __init__(self, pp, bits):
		self.p = pp
		self.dim = len(pp)
		self.bits = bits

	def __lt__(self, other):
		i = 0
		a = self.p
		b = other.p
		x = a[i] ^ b[i]
		for j in range(1, self.dim):
			y = a[j] ^ b[j]
			if less_msb(x, y):
				i = j
				x = y
		return a[i] < b[i]
		#return zorder(self.p, other.p) # this way sorts according to x axis

	def __repr__(self):
		return str(self.p)

	def __getitem__(self, idx):
		return self.p[idx]

class MortonFloat:
	def __init__(self, pp):
		self.p = pp
		self.dim = len(pp)
		self.computeCode()

	def computeCode(self):
		self.code = 0
		up = tuple([unpack(">I", pack(">f", self.p[i]))[0] for i in range(self.dim)])
		bits = 32 * self.dim
		for b in range(bits):
			ibits = reduce((lambda x, y: x | y), [((up[i] >> (bits - 1 - b)) & 1) << i for i in range(self.dim)])
			self.code = (self.code << self.dim) | ibits

	def __lt__(self, other):
		return self.code < other.code

	def __repr__(self):
		return str((self.p[0], self.p[1]))

	def __getitem__(self, idx):
		return self.p[idx]

class MortonFloatQuick:
	def __init__(self, pp):
		self.p = pp
		self.dim = len(pp)

	def __lt__(self, other):
		x = 0
		d = 0
		for j in range(self.dim):
			y = xormsb2(self.p[j], other.p[j])
			if x < y:
				x = y
				d = j
		return self.p[d] < other.p[d]

	def __getitem__(self, idx):
		return self.p[idx]

def xormsb(a, b):
	abits = unpack(">I", pack(">f", a))[0]
	bbits = unpack(">I", pack(">f", b))[0]
	x = (abits>>23) & 0x00FF
	y = (bbits>>23) & 0x00FF
	if x == y:
		z = msdb(abits & 0x7FFFFF, bbits & 0x7FFFFF) # 23 bits
		x = x - z
		return x
	if y < x:
		return x
	return y

def xormsb2(a, b):
	xm, xe = frexp(a)
	ym, ye = frexp(b)
	if xe == ye:
		#z = msdb2(decfrac2man(xm), decfrac2man(ym))
		#xe = xe - z
		#return xe
		##-----------
		if ym == xm:
			return 0
		else:
			ai = unpack(">q", pack(">d", xm))[0]
			bi = unpack(">q", pack(">d", ym))[0]
			zi = unpack(">q", pack(">d", 0.5))[0]
			abi = (ai^bi)|zi
			ab = unpack(">d", pack(">q", abi))[0]
			ym, ye = frexp(ab - 0.5)
			return ye + xe
	if ye < xe:
		return xe
	return ye

def decfrac2man(x):
	N = 32
	result = 0
	for i in range(N):
		t = x * 2
		result = (result << 1) | int(t)
		x = t - int(t)
	return result

def msdb2(a, b):
	ab = a ^ b
	N = 32
	f = 1<<(N-1)
	for i in range(N):
		if f & (ab << i) > 0:
			return i
	return 0

def msdb(a, b):
	ab = a ^ b
	N = 24
	for m in range(N):
		if not 0x800000 > (ab << m):
			return N - 1 - m
	return 0

def less_msb(x, y):
	return x < y and x < (x ^ y)

def zorder(a, b):
	j = 0
	k = 0
	x = 0
	dim = len(a)
	for k in range(dim):
		y = a[k] ^ b[k]
		if op(x, y):
			j = k
			x = y
	return a[j] - b[j]


"""
see here for reference:
https://stackoverflow.com/questions/45332056/decompose-a-float-into-mantissa-and-exponent-in-base-10-without-strings
"""
def fexp(number):
	(sign, digits, exponent) = Decimal(number).as_tuple()
	return len(digits) + exponent - 1

def fman(number):
	return Decimal(number).scaleb(-fexp(number)).normalize()