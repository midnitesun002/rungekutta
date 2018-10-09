# To test the speed of various morton sorting algos

from Morton_Naive import *

import sys, getopt
import random

try:
	opts, args = getopt.getopt(sys.argv[1:], "n:a:s:")
except getopt.GetoptError as err:
	print("incorrect arguments")
	print(err)
	sys.exit(2)

N = 10
bits = 12
HIGH = 2**(bits/2) - 1
method = 1
show = False
for opt, arg in opts:
	if opt == "-n":
		N = int(arg)
	elif opt == "-a":
		method = int(arg)
	elif opt == "-s":
		random.seed(int(arg))
	elif opt == "-p":
		show = True
	else:
		assert False, "unhandled option"

if method == 1:
	codes = [MortonNaive((random.randint(0, HIGH), random.randint(0, HIGH)), bits) for i in range(N)]
elif method == 2:
	codes = [MortonQuick((random.randint(0, HIGH), random.randint(0, HIGH)), bits) for i in range(N)]

list.sort(codes)
if show:
	print(codes)