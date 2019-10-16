maxd = pow(10, 5)
prime_factors = [[] for i in range(maxd)]

for i in range(2, maxd):
	if len(prime_factors[i])==0:	# check if "i" is prime
		for j in range(i, maxd, i):	# all the multiple of prime number i, will definitely have i as one of its prime prime_factors 
			prime_factors[j].append(i)
print(prime_factors[51])