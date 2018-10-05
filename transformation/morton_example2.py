
from Morton import *
import matplotlib.pyplot as plt
import random

bits = 12
N = 10000
a, b = 4.5, 17.3
center = 14
stdev = 3

# Create the points
#xp = [random.uniform(a, b) for i in range(N)]
#yp = [random.uniform(a, b) for i in range(N)]
xp = [random.gauss(center, stdev) for i in range(N)]
yp = [random.gauss(center, stdev) for i in range(N)]

# Normalize points to bits
xmax, xmin = max(xp), min(xp)
ymax, ymin = max(yp), min(yp)
dx, dy = xmax - xmin, ymax - ymin
xb = list(map(lambda t: int((t - xmin) / dx * (2**bits - 1)), xp))
yb = list(map(lambda t: int((t - ymin) / dy * (2**bits - 1)), yp))

# Create morton codes for points
mm = [MortonI2d(x, y, bits) for x, y in zip(xb, yb)]
ms = sorted(mm)
# Note that there will be a difference between iterating over ms vs mm
# mm is unsorted, so points will move randomly if tracing lines between them
# ms is sorted, and appear "neat and orderly" when tracing lines between points
mx = [m.x for m in ms]
my = [m.y for m in ms]

lower_x = int((7 - xmin) / dx * (2**bits-1))
upper_x = int((9 - xmin) / dx * (2**bits-1))
lower_y = 0
upper_y = 2**bits-1
lower_z = MortonI2d(lower_x, lower_y, bits).getCode()
upper_z = MortonI2d(upper_x, upper_y, bits).getCode()

xquery = list(filter(lambda m: lower_x < m.x and m.x < upper_x, ms))
qx = [m.x for m in xquery]
qy = [m.y for m in xquery]

# Plot
#plt.plot(xb, yb, '-')
#plt.plot(mx, my, '-')
#plt.plot(qx, qy, 'rx')
#plt.show()

print(len(set([m.getCode() for m in mm])))