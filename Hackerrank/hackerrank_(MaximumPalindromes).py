'''
	Problem url: https://www.hackerrank.com/challenges/maximum-palindromes/problem
'''

ip = open("testdata.txt", "r")

def input():
	return ip.readline().strip()

from collections import Counter
from functools import reduce
from operator import mul
import math

L, M = 26, 1000000007
def initialize(s):
	n, z = len(s), ord('a')
	S, F, I = [[0] * L for _ in range(n + 1)], [1] * n, [1] * n
	# print(S, F, I)
	for i, v in enumerate(s, 1):
		for j in range(L):          # 2D array of character counts
			S[i][j] = S[i - 1][j] + (j == ord(v) - z)
	print(S)
	for i in range(1, n):
		F[i] = F[i - 1] * i % M     # modular factorial
		I[i] = pow(F[i], M - 2, M)  # modular inverse of factorial
	return(S, F, I)
	
def answerQuery(l, r):
	c, s, d = 0, 0, 1
	for j in [S[r][i] - S[l - 1][i] for i in range(L)]:
		c += j % 2                  # count of center characters
		s += j // 2                 # count of side characters
		d *= I[j // 2]              # "denominators"
	return((c or 1) * F[s] * d % M)

s = input()
S, F, I = initialize(s)
q = int(input())

for _ in range(q):
	fn = lambda x:int(x)-1
	l, r = map(int, input().split())
	print(answerQuery(l, r))