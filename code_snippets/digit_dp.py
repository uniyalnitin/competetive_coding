'''

we need to check if the number we have formed contains atleast K distinct numbers or not . 
This certainly points us to keep a bitmask of length 9 where ith bit stores existance of digit i in the number.
(we dont need ‘0’ mentioned in the question)

Incase the above condition is true , then the number should also be divisible by atleast K of digits used in making it . 
To check divisibility we need the actual number but we cant pass such numbers in recursive call :confused: . 
Then how will we check this condition at our base case? so the answer is we dont need to pass the whole number , 
we can actually pass the number%(LCM(1,2,3,4,5,6,7,8,9)) i.e. number%2520.
'''

arr = [7, 7, 7]
k = 2

def check(mask, mod_val):
	count = 0
	i=0
	while mask:
		bit = mask & 1
		mask = mask>>1
		if bit and mod_val%i==0:
			count += 1
		i += 1
	return count >= k

def solve(length, is_equal, mask, mod_val):
	'''
	length : length of the array
	is_equal: is_equal stores boolean value if the number we have made until now is equal to R or not
	mask : to check if the number we have formed contains atleast K distinct numbers or not
	mod_val: To check divisibility by atleast K of digits used in making it 
	'''
	if length==0:
		if check(mask, mod_val):
			return 1
		return 0
	sol = 0
	if not is_equal:
		for i in range(10):
			sol += solve(length-1, 0, mask if i==0 else mask | 1 << i, (mod_val*10+i)%2520)
	else:
		for i in range(arr[length-1]+1):
			if i < arr[length-1]:
				sol += solve(length-1, 0, mask if i==0 else mask| 1<<i, (mod_val*10+i)%2520)
			else:
				sol += solve(length-1, 1, mask if i==0 else mask| 1<<i, (mod_val*10+i)%2520)
	return sol

ans = solve(len(arr), 1, 0, 0)
print(ans)

# *****************************************************************************************************************************

import time
a, b, s = 5, 17, 5

def num_digits(n):
	count = 0
	while n:
		count += 1
		n = n//10
	return count

def check(val):
	global keep
	add = 0
	n = val
	while val:
		add += val%10
		val = val//10
	if add==s:
		keep.add(n)
		return 1
	return 0

def solve(length, is_equal, val):
	global a

	if length==0:
		return check(val)
	sol = 0
	if not is_equal:
		for i in range(10):
			sol += solve(length-1, 0, val*10 + i)
	else:
		temp = a%(10**length)//(10**(length-1))
		for i in range(temp+1):
			if i<temp:
				sol += solve(length-1, 0, val*10+i)
			else:
				sol += solve(length-1, 1, val*10+i)
	return sol 

a = 114
keep = set()
ans1 = solve(3, 1, 0)
k1 = keep
a = 4
keep = set()
ans2 = solve(2, 1, 0)
k2 = keep
print(ans1-ans2)
print(min(k1-k2))
# print(ans1)