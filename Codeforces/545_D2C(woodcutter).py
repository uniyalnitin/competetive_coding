'''
	Problem Url: https://codeforces.com/contest/545/problem/C
	Idea : Greedy (start placing from left)
'''
n = int(input())
X, H = [0]*n, [0]*n

for i in range(n):
	X[i], H[i] = map(int, input().split())

s = 2
 
for i in range(1, n - 1):
	x, h = X[i], H[i]
	if x - h > X[i-1]:	# is left available
		s += 1
	elif x + h < X[i+1]: # is right available
		s += 1
		X[i] += h # occupy the right till h

print(s if n > 1 else 1)