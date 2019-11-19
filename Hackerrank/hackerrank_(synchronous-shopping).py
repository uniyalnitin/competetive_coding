'''
	Problem Url: https://www.hackerrank.com/challenges/synchronous-shopping/problem
	Idea: Use Dijkastra 
	trick: The key here is not just about find the shortest path from 1 to n.
			It's about find the shortest path from the state at node 1 to the 2^k -1 state at node n. 
			state is the mask to represent the Fishesh collected
'''

stdin = open("testdata.txt", "r")

# from sys import stdin
import sys

sys.setrecursionlimit(10**9)
def input():
	return stdin.readline().strip()

from collections import defaultdict
import heapq

INF = 1234567890

n, m, k = map(int, input().split())

total = 1 << k

fish = [0]*(n+1)

for i in range(1, n+1):
	fishes = list(map(int, input().split()))
	for j in range(1, len(fishes)):
		fish[i] |= 1 << (fishes[j]-1)

graph = defaultdict(lambda: defaultdict(int))
for i in range(m):
	a, b, c = map(int, input().split())
	graph[a][b] = c
	graph[b][a] = c

dist = defaultdict(lambda: defaultdict(lambda: int(INF)))

def dijkastra():
	pq = []

	heapq.heappush(pq, [0, [1, fish[1]]])	# wt, [node, state]
	dist[1][fish[1]] = 0	# dist[node][state] => smallest weights to achieve state at node i

	while pq:
		wt_node, [node, state] = heapq.heappop(pq)
		wt_node = -wt_node

		if wt_node != dist[node][state]:
			continue
		for cnode, wt_cnode in graph[node].items():
			next_state = state | fish[cnode]

			if dist[cnode][next_state] > wt_cnode + wt_node:
				dist[cnode][next_state] = wt_cnode + wt_node
				heapq.heappush(pq, [-dist[cnode][next_state], [cnode, next_state]])

dijkastra()

ans = INF

for i in range(total):
	for j in range(i, total):
		if (i|j) == ((1 << k)-1):
			ans = min(ans, max(dist[n][i], dist[n][j]))
print(ans)