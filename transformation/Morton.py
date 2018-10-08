
from decimal import Decimal

class MortonI2d:
	# Unsigned Integer inputs
	def __init__(self, xx, yy, bits):
		self.x = xx
		self.y = yy
		self.bits = bits
		self.computeCode()

	def __repr__(self):
		return "(%d, %d)" % (self.x, self.y)

	def computeCode(self):
		self.code = 0
		for b in range(self.bits):
			self.code = (self.code << 2) | ((self.x >> (self.bits - 1 - b)) & 1) << 0 | ((self.y >> (self.bits - 1 - b)) & 1) << 1

	def getCode(self):
		return self.code
	
	def printCode(self):
		return [(self.code >> (2 * self.bits - 1 - b)) & 1 for b in range(2 * self.bits)]

	def __lt__(self, other):
		return self.code < other.code

class MortonIN2d:
	# Signed integer inputs
	def __init__(self, xx, yy, bits):
		self.x = xx
		self.y = yy
		self.bits = bits
		self.getCode()

	def __repr__(self):
		return "(%d, %d)" % (self.x, self.y)

	def getCode(self):
		self.code = 0
		local_x = self.x
		if self.x < 0:
			local_x &= ~(1<<(self.bits-1))
		local_y = self.y
		if self.y < 0:
			local_y &= ~(1<<(self.bits-1))
		for b in range(self.bits):
			self.code = (self.code << 2) | ((local_x >> (self.bits - 1 - b)) & 1) << 0 | ((local_y >> (self.bits - 1 - b)) & 1) << 1
		if self.y < 0:
			self.code &= ~(1<<(2*self.bits-1))
	
	def printCode(self):
		return [(self.code >> (2 * self.bits - 1 - b)) & 1 for b in range(2 * self.bits)]

	def __lt__(self, other):
		return self.code < other.code

class MortonI3d:
	def __init__(self, xx, yy, zz, bits):
		self.x = xx
		self.y = yy
		self.z = zz
		self.bits = bits
		self.getCode()

	def __repr__(self):
		return "(%d, %d, %d)" % (self.x, self.y, self.z)

	def getCode(self):
		self.code = 0
		for b in range(self.bits):
			self.code = (self.code << 3) | ((self.x >> (self.bits - 1 - b)) & 1) << 0 | ((self.y >> (self.bits - 1 - b)) & 1) << 1 | ((self.z >> (self.bits - 1 - b)) & 1) << 2

	def printCode(self):
		return [(self.code >> (3 * self.bits - 1 - b)) & 1 for b in range(3 * self.bits)]

	def __lt__(self, other):
		return self.code < other.code

def fexp(number):
	(sign, digits, exponent) = Decimal(number).as_tuple()
	return len(digits) + exponent - 1

def fman(number):
	return Decimal(number).scaleb(-fexp(number)).normalize()