# To plot the order of various morton algos

from Morton_Naive import *
import matplotlib.pyplot as plt

import sys, getopt
import random

try:
	opts, args = getopt.getopt(sys.argv[1:], "b:a:s:pr")
except getopt.GetoptError as err:
	print("incorrect arguments")
	print(err)
	sys.exit(2)

N = 10
bits = 4
method = 1
plot = False
randomize = False
for opt, arg in opts:
	if opt == "-a":
		method = int(arg)
	elif opt == "-p":
		plot = True
	elif opt == "-b":
		bits = int(arg)
	elif opt == "-r":
		randomize = True
	else:
		assert False, "unhandled option"

if method == 1:
	if randomize:
		codes = [MortonNaive((random.randint(0, 2**bits-1), random.randint(0, 2**bits-1)), bits) for x in range(2**bits) for y in range(2**bits)]
	else:
		codes = [MortonNaive((x, y), bits) for x in range(2**bits) for y in range(2**bits)]
elif method == 2:
	if randomize:
		codes = [MortonQuick((random.randint(0, 2**bits-1), random.randint(0, 2**bits-1)), bits) for x in range(2**bits) for y in range(2**bits)]
	else:
		codes = [MortonQuick((x, y), bits) for x in range(2**bits) for y in range(2**bits)]
elif method == 3:
	if randomize:
		codes = [MortonFloat((random.random(), random.random())) for x in range(2**bits) for y in range(2**bits)]
	else:
		codes = [MortonFloat((x/2**bits, y/2**bits)) for x in range(2**bits) for y in range(2**bits)]
elif method == 4:
	if randomize:
		codes = [MortonFloatQuick((random.random(), random.random())) for x in range(2**bits) for y in range(2**bits)]
	else:
		codes = [MortonFloatQuick((x/2**bits, y/2**bits)) for x in range(2**bits) for y in range(2**bits)]
elif method == 5:
	codes = [MortonSpecial((x/2**bits, y/2**bits)) for x in range(2**bits) for y in range(2**bits)]

list.sort(codes)
if plot:
	for i in range(len(codes)):
		plt.plot(codes[i][0], codes[i][1], 'rx')
	for i in range(len(codes) - 1):
		plt.plot([codes[i][0], codes[i+1][0]], [codes[i][1], codes[i+1][1]], 'b-')
	plt.show()
#print(codes)
