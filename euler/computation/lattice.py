#!/usr/local/bin/python3
import numpy as np
import matplotlib.pyplot as plt
import time, sys, random, colorama

np.set_printoptions(suppress=True)

def path(x):
	f = np.ones(x**2).reshape(x,x)
	for j in range(1, len(f)):
		print("Step:", j)
		for i in range(1, len(f[j])):
			f[j][i] = f[j][i-1] + f[j-1][i]		
		print(f, end="\r")
	print(f[-1][-1])

def gen():
	c = random.randint(0,1)
	d = random.randint(0,1)
	if (d == 0):
		d -= 1
	return c,d

def visualize(x):
	f = np.zeros(x**2).reshape(x,x)
	count, bg, m = 0, 0, 1
	pos = [0,0]

	for i in range(f.shape[0]):
		for j in range(f.shape[1]):
			f[i][j] = bg
	try:
		r = sys.argv[3]
	except:
		r = "d"

	while (f[-1][-1] == bg):
		f[pos[0]][pos[1]] = m 
		c, d = gen()

		# setting boundaries
		if r == "r":
			if (pos[c] == 0) and (d == -1):
				d = 1
			if (pos[c] == len(f)-1) and (d == 1):
				d = -1
			pos[c] += 1 * d
		# old straightforward movement
		else:
			if (pos[c] < (len(f)-1)):
				pos[c] += 1
			else:
				pos[(c+1)%2] += 1

		count += 1
		m += 20
		"""
		count += 1
		if (count%(x//10)==0):
			plt.savefig(f"{count}.png")
		"""
		"""
		# progress
		if (count % 100 == 0):
			plt.imshow(f)
			plt.show()
		"""
		print(pos)
	plt.imshow(f)
	plt.show()
	print(count)

v = sys.argv[1]	
if (v in "visualization"):
	x = int(sys.argv[2]) + 1
	visualize(x)
else:
	x = int(sys.argv[1]) + 1
	path(x)
