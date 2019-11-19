'''
	Problem Url: https://www.hackerrank.com/challenges/beautiful-path/problem
	Solution: Use DFS to explore the all state (i.e. [node][c1 or c2 or ...])
'''

import sys
from collections import defaultdict

sys.setrecursionlimit(pow(10, 9))

n, m = map(int, input().split())

graph = defaultdict(list)

for _ in range(m):
	u, v, c = map(int, input().split())
	graph[u].append([v, c])
	graph[v].append([u, c])

a, b = map(int, input().split())

def dfs(x, cost):
	visited = [[0]*1024 for _ in range(1001)]
	visited[x][cost] = 1
	stack = [[x, cost]]
	while stack:
		x, cost = stack.pop()
		for child, wt in graph[x]:
			c_cost = cost|wt
			if not visited[child][c_cost]:
				visited[child][c_cost] = 1
				stack.append([child, c_cost])

	for i in range(1024):
		if visited[b][i] == 1:
			return i 
	return -1
ans = dfs(a, 0)
print(ans)
