'''
	Problem Url: https://www.hackerrank.com/challenges/clique/problem
	Idea: Turan's Theorem
	Turán's theorem states that if a graph on n vertices doesn't contain
	an (r+1)-clique then it has at most ⌊r−1*n*n/(r*2)⌋ edges

	for large values:
		m* = (N*N - (N%r)*NR*NR - (r - (N%r))*nr*nr)/2
'''

import math

def predicate(r):
	NR = math.ceil(N/r)
	nr = math.floor(N/r)
	
	m = (N*N - (N%r)*NR*NR - (r - (N%r))*nr*nr)/2
	# m = (r-1)*N*N/(2*(r))
	return E > int(m)

def bs(l, r):
	while l < r:
		m = l + r + 1 >> 1
		if predicate(m):
			l = m
		else:
			r = m - 1
	return l

t = int(input())

for _ in range(t):
	N, E = map(int, input().split())
	ans = bs(0, N)
	print(ans+1)