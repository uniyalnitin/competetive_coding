def factorize(n): 
	pf = []
	count =  0
	while ((n % 2 > 0) == False):  
		n >>= 1  
		count += 1 

	if (count > 0): 
		pf.append(2) 
  
	# check for all the possible 
	# numbers that can divide it 
	for i in range(3, int(math.sqrt(n)) + 1, 2): 
		count = 0; 
		while (n % i == 0):  
			count += 1
			n = n//i 
		if (count > 0): 
			pf.append(i) 
		# i += 2
	if n > 2:
		pf.append(n)
	return pf