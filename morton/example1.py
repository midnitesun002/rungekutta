
from decimal import Decimal

"""
see here for reference:
https://stackoverflow.com/questions/45332056/decompose-a-float-into-mantissa-and-exponent-in-base-10-without-strings
"""
def fexp(number):
	(sign, digits, exponent) = Decimal(number).as_tuple()
	return len(digits) + exponent - 1

def fman(number):
	return Decimal(number).scaleb(-fexp(number)).normalize()

num = 21.3
print(fexp(num))
print(fman(num))
