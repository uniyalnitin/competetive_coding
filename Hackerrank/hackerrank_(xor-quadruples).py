'''
	problem Url: https://www.hackerrank.com/challenges/xor-quadruples/problem
	Idea: DP and Meet in the middle technique
	Editorial link-: https://fizzbuzzer.com/beautiful-quadruples-challenge/
'''
stdin = open("testdata.txt", "r")

# from sys import stdin
import sys

sys.setrecursionlimit(10**9)
def input():
	return stdin.readline().strip()

from collections import defaultdict
from itertools import permutations

inp = list(map(int, input().split()))
inp.sort()
A, B, C, D = inp 

# total[B] holds the number of pairs {a, b} such that a <= b and 1 <= a <= A and 1 <=b <= B
total = [0]*3010

# cnt[B][x] holds holds the number of pairs {a, b} such that a <= b and a^b = x
cnt = [[0]*4100 for _ in range(3010)]

for i in range(1, A+1):
	for j in range(i, B+1):
		total[j] += 1
		cnt[j][i^j] += 1	# total number of pairs that ends with j and xor I^J

for i in range(1, 3010):
	total[i] += total[i-1]
	for j in range(4100):
		cnt[i][j] += cnt[i-1][j] # adding all the counts of the numbers

res = 0
for i in range(1, C+1):
	for j in range(i, D+1):
		# exclude the pairs {a, b} which have same xor (i.e. a^b = c^d)
		res += total[i] - cnt[i][i^j]
print(res)