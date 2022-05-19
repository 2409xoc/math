#!/usr/local/bin/python3
import math, sys

# Pollard Rho's Algorithm - integer factorization
def g(x, n):
	return (x**2 + 1) % n

def pollard(n):
	d,x,y = 1,2,2
	while (d == 1):
		x = g(x, n)
		y = g(g(y, n), n)	
		d = math.gcd(abs(x-y), n)
	return d

def rho():
	fl = []
	while (n > 1):
		f = pollard(n)
		n //= f
		fl.append(f)

	print(fl)

# (calling function within itself - not exactly recursion) - integer prime factorization
def isprime(n):
	if (n == 2) or (n == 3):
		return True
	if (n%2 == 0) or (n%3 == 0):
		return False
	i = 5
	while (i <= int(n**0.5)):
		if (n%i == 0) or (n%(i+2) == 0):
			return False
		i += 6
	return True

def primes(n):
	l = []
	while (isprime(n) != True):
		for j in range(2, n):
			if (n%j == 0) and (isprime(j) == True):
				n //= j		
				l.append(j)	
	if (n != 1):	
		l.append(n)
	l.sort()
	return l

def factor(n):
	f = 1
	pl = primes(n)
	print(pl)
	while (len(pl) > 0):
		j = pl[0]
		f *= (pl.count(j)	+ 1)
		for j in range(pl.count(j)):
			del pl[0]

factor(int(sys.argv[1]))
