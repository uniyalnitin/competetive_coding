'''
problem_url-: https://atcoder.jp/contests/abc143/tasks/abc143_e
editorial -: https://codeforces.com/blog/entry/70703
'''
import sys

inp = sys.stdin
# inp = open("testdata.txt", "r")
def input():
	return inp.readline().strip()

	
n, m, l = map(int, input().split())

def warshall_floyd(d):
	for k in range(n):
		for i in range(n):
			for j in range(n):
				d[i][j] = min(d[i][j],d[i][k] + d[k][j])
	return d

adjl = [[float('inf') for j in range(n)] for i in range(n)]
for i in range(n):
	adjl[i][i] = 0

for _ in range(m):
	a, b, c = map(int, input().split())
	adjl[a-1][b-1] = c
	adjl[b-1][a-1] = c

adjl = warshall_floyd(adjl)

for i in range(n):
	for j in range(n):
		if i==j: adjl[i][j] = 0
		else: adjl[i][j] = 1 if adjl[i][j] <= l else float("inf")

adjl = warshall_floyd(adjl)

q = int(input())

for _ in range(q):
	a, b = map(int, input().split())
	ans = adjl[a-1][b-1]
	print(-1 if ans==float("inf") else ans-1)