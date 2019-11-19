'''
Problem Url: https://codeforces.com/contest/152/problem/B
Idea: Almost Binary Search
'''

n, m = map(int, input().split())

xc, yc = map(int, input().split())

k = int(input())

total = 0
def onField(x, y):
	'''
		Is Inside rectangle n x m
	'''
	return 1 <= x<= n and 1 <= y <= m 

for i in range(k):
	dx, dy = map(int, input().split())

	cof = 1100000000
	while(cof):
		while onField(xc + cof * dx, yc + cof * dy):
			xc = xc + cof * dx;
			yc = yc + cof * dy;
			total += cof;
		cof = cof // 2
print(total)