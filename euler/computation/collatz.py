#!/usr/local/bin/python3

import sys

l = []
x = int(sys.argv[1])
for n in range(1, x):
	i = n
	count = 0
	while (n != 1):
		if (n%2 == 0):
			n /= 2 
		else:
			n = 3*n + 1
		count += 1
	print(i, count)
	l.append(count)

m = l.index(max(l))+1
mm = [m]
print("Max:", m, "\nSequence Amount:", max(l)) 
while (m > 1):
	if (m%2 == 0):
		m //= 2
	else:
		m = 3*m+1
	mm.append(m)
print(mm)	


