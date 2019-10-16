'''
Miller-Rabin primarility test
step 1- for the given n find k and m in "n-1 = 2^k * m"
step 2- choose a random a between 2 < a < n-1
step 3- compute b[0] = a^m % n, if b[0]= +- 1 check for other test, else further compute b[i] = b[i-1]^2 % n
contd.. if b[i]=1 return Not Prime , else if b[i]==1 return Prime else compute b[i+1]
'''
from random import randint

def isPrime(n, k=5): # miller-rabin
	if n < 2: return False
	for p in [2,3,5,7,11,13,17,19,23,29]:
		if n % p == 0: return n == p
	s, d = 0, n-1
	while d % 2 == 0:
		s, d = s+1, d//2
	for i in range(k):
		x = pow(randint(2, n-1), d, n)
		if x == 1 or x == n-1: continue
		for r in range(1, s):
			x = (x * x) % n
			if x == 1: return False
			if x == n-1: break
		else: return False
	return True

print(isPrime(3121))