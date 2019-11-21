'''
	Edmonds-karp Max Flow Algorithm
	This algorithm uses BFS to find the augmented path between source and sink. 
	We than find the bottlenect value of this path, and agument this path.
	Keep find augmented paths, until there are None left.
	return the sum of all bottle neck values or the sum of flow of all edges attached to sink
'''

stdin = open("testdata.txt", "r")
# from sys import stdin

def input():
	return stdin.readline().strip()

from collections import defaultdict, deque

#Edmonds-Karp Algorithm
def max_flow(C, s, t):
	n = len(C) # C is the capacity matrix
	F = [[0] * n for i in range(n)]	# F is the flow matrix
	path = bfs(C, F, s, t)	# augmented path
	while path:	
		# run bfs until there are no agumented path
		flow = min(C[u][v] - F[u][v] for u,v in path)	# Get the bottleneck value of the path
		for u,v in path:
			# Augmenting the path
			F[u][v] += flow # increase the flow in forward edges
			F[v][u] -= flow # decrease the flow in reverse edges
		path = bfs(C, F, s, t)
	return sum(F[s][i] for i in range(n))	# return the sum of all Filled nodes that are attached to sink

##search augmenting path by using BFS
def bfs(C, F, s, t):
	queue = deque([s])
	paths = defaultdict(list)

	if s == t:
		return paths[s]
	while queue:
		u = queue.popleft()
		for v in graph[u]:
			if(C[u][v]-F[u][v]>0) and v not in paths:
				paths[v] = paths[u] + [(u,v)]
				if v == t:
					return paths[v]	# return the path as soon as sink is reached
				queue.append(v)
	return None	# Sink is not reachable from source
	
# make a capacity graph
# node   s   o   p   q   r   t
n = 6; s= n-1; t = n-2;

edges = [(s, 0, 10),
		(s, 1, 10),

		(2, t, 10),
		(3, t, 10),

		(0, 1, 2),
		(0, 2, 4),
		(0, 3, 8),
		(1, 3, 9),
		(3, 2, 6),
	]

C = [[0]*n for i in range(n)]

graph = defaultdict(lambda:defaultdict(int))

for u, v, w in edges:
	graph[u][v] = w
	graph[v][u] = 0
	C[u][v] = w

max_flow_value = max_flow(C, s, t)
print("Edmonds-Karp algorithm")
print("max_flow_value is: ", max_flow_value)