#!/usr/local/bin/python3
import time
from factorization import *

# generating triangular numbers
i = 2
mf = 0
while (mf < 500):
	j = sum(range(i))
	fv = factor(j)
	if (fv > mf):
		mf = fv
	print(i, j, fv)
	i += 1
