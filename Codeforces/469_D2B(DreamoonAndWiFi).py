'''
Problem Url: https://codeforces.com/contest/476/problem/B
Idea: Permutation and Combination
'''

import math

s1 = input()
s2 = input()

plus, minus = s1.count('+'), s1.count('-')

pre_plus = s2.count('+'); pre_minus = s2.count('-')

req_plus, req_minus = plus- pre_plus, minus - pre_minus

if req_minus < 0 or req_plus < 0:
	print('%.12f'%0)
else:
	unknowns = len(s1) - (pre_minus + pre_plus)

	if unknowns == 0:
		print('%.12f'%1)
	else:
		den = pow(2, unknowns)
		num = math.factorial(unknowns)/(math.factorial(req_plus)*math.factorial(req_minus))
		ans = num/den
		print('%.12f'%ans)