'''
	Original Link: https://codereview.stackexchange.com/questions/186077/increase-the-efficiency-of-a-matching-algorithm
'''

from collections import defaultdict, deque

def maximum_matching(graph):
	"""Find a maximum unweighted matching in a bipartite graph. The input
	must be a dictionary mapping vertices in one partition to sets of
	vertices in the other partition. Return a dictionary mapping
	vertices in one partition to their matched vertex in the other.

	"""
	# The two partitions of the graph.
	U = set(graph.keys())
	V = set.union(*graph.values())

	# A distinguished vertex not belonging to the graph.
	nil = object()

	# Current pairing for vertices in each partition.
	pair_u = dict.fromkeys(U, nil)
	pair_v = dict.fromkeys(V, nil)

	# Distance to each vertex along augmenting paths.
	dist = {}
	inf = float('inf')

	def bfs():
		# Breadth-first search of the graph starting with unmatched
		# vertices in U and following "augmenting paths" alternating
		# between edges from U->V not in the matching and edges from
		# V->U in the matching. This partitions the vertexes into
		# layers according to their distance along augmenting paths.
		queue = deque()
		for u in U:
			if pair_u[u] is nil:
				dist[u] = 0
				queue.append(u)
			else:
				dist[u] = inf
		dist[nil] = inf
		while queue:
			u = queue.pop()
			if dist[u] < dist[nil]:
				# Follow edges from U->V not in the matching.
				for v in graph[u]:
					# Follow edge from V->U in the matching, if any.
					uu = pair_v[v]
					if dist[uu] == inf:
						dist[uu] = dist[u] + 1
						queue.append(uu)
		return dist[nil] is not inf

	def dfs(u):
		# Depth-first search along "augmenting paths" starting at
		# u. If we can find such a path that goes all the way from
		# u to nil, then we can swap matched/unmatched edges all
		# along the path, getting one additional matched edge
		# (since the path must have an odd number of edges).
		if u is not nil:
			for v in graph[u]:
				uu = pair_v[v]
				if dist[uu] == dist[u] + 1: # uu in next layer
					if dfs(uu):
						# Found augmenting path all the way to nil. In
						# this path v was matched with uu, so after
						# swapping v must now be matched with u.
						pair_v[v] = u
						pair_u[u] = v
						return True
			dist[u] = inf
			return False
		return True

	while bfs():
		for u in U:
			if pair_u[u] is nil:
				dfs(u)
	return {u: v for u, v in pair_u.items() if v is not nil}

graph = {16: {1, 2, 4, 8}, 
			2 : {1, 2}, 
			4 : {1, 2, 4},
			1 : {1, },
			32 : {1, 2, 4, 8}
		}

MAXN = pow(10, 5)+1
divisors = [{1, } for i in range(MAXN)]

for i in range(2, MAXN):
	for j in range(i, MAXN, i):
		divisors[j].add(i)

x = maximum_matching(graph)
print(len(x))