
from Morton import *
import matplotlib.pyplot as plt
import random


bits = 4
points = [None for i in range(2**(2*bits))]
for x in range(2**bits):
	for y in range(2**bits):
		#points[x*2**bits + y] = MortonIN2d(x-2**(bits-1), y-2**(bits-1), bits)
		points[x*2**bits + y] = MortonI2d(x, y, bits)

random.shuffle(points)
list.sort(points)
print(points)
print(MortonI2d(5, 9, 4).printCode())
print(MortonI3d(5, 9, 1, 4).printCode())
print(MortonI3d(1, 2, 3, 4).printCode())
print(MortonI3d(3, 2, 1, 4).printCode())
print(MortonI3d(4, 4, 4, 4).printCode())

for i in range(len(points)):
	plt.plot(points[i].x, points[i].y, 'rx')
for i in range(len(points) - 1):
	plt.plot([points[i].x, points[i+1].x], [points[i].y, points[i+1].y], 'b-')

plt.show()