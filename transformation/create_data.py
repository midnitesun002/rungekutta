
import struct
import random

count = 500
axes = 3
center = 15
stdev = 2

with open("data.bin", "wb") as file:
	for c in range(count):
		for a in range(axes):
			file.write(struct.pack("d", random.gauss(center, stdev)))
			file.write(struct.pack("d", random.gauss(center, stdev)))

print("Done")