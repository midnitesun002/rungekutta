# To plot the order of various morton algos

from Morton_Naive import *
import matplotlib.pyplot as plt

import sys, getopt

try:
	opts, args = getopt.getopt(sys.argv[1:], "b:a:s:p")
except getopt.GetoptError as err:
	print("incorrect arguments")
	print(err)
	sys.exit(2)

N = 10
bits = 4
method = 1
plot = False
for opt, arg in opts:
	if opt == "-a":
		method = int(arg)
	elif opt == "-p":
		plot = True
	elif opt == "-b":
		bits = int(arg)
	else:
		assert False, "unhandled option"

if method == 1:
	codes = [MortonNaive((x, y), bits) for x in range(2**bits) for y in range(2**bits)]
elif method == 2:
	codes = [MortonQuick((x, y), bits) for x in range(2**bits) for y in range(2**bits)]
elif method == 3:
	codes = [MortonFloat((x/2**bits, y/2**bits)) for x in range(2**bits) for y in range(2**bits)]
elif method == 4:
	codes = [MortonFloatQuick((x/2**bits, y/2**bits)) for x in range(2**bits) for y in range(2**bits)]

list.sort(codes)
if plot:
	for i in range(len(codes)):
		plt.plot(codes[i][0], codes[i][1], 'rx')
	for i in range(len(codes) - 1):
		plt.plot([codes[i][0], codes[i+1][0]], [codes[i][1], codes[i+1][1]], 'b-')
	plt.show()
#print(codes)