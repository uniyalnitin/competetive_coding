from collections import defaultdict

stdin = open("testdata.txt", "r")

N, m = map(int, stdin.readline().split())

adj = defaultdict(list)

for _ in range(m):
	a, b = map(int, stdin.readline().split())
	adj[a].append(b)

next = 0 # Next index.
ids = [None] * N #assign the id to each vertex as discovered ( discovered time )
lowlink = [None] * N #minimum low id/ low link node that is part of current SCC rechable from a node
onstack = [False] * N 
stack = []
nextgroup = 0 # Next SCC ID.
groups = [] # SCCs: list of vertices.
groupid = {} # Map from vertex to SCC ID.

# Tarjan's algorithm.
def sconnect_recursive(at):
	global next, nextgroup
	ids[at] = next
	lowlink[at] = next
	next += 1
	stack.append(at)
	onstack[at] = True
	for to in adj[at]:
		if ids[to] == None:
			sconnect_recursive(to)
		if onstack[to]:
			lowlink[at] = min(lowlink[at], lowlink[to])
			# lowlink[at] = min(lowlink[at], ids[to])
	if ids[at] == lowlink[at]:
		com = []
		while True:
			node = stack.pop()
			onstack[node] = False
			com.append(node)
			groupid[node] = nextgroup
			if node == at: break
		groups.append(com)
		nextgroup += 1

def sconnect_iterative(v):
	global next, nextgroup
	work = [(v, 0)] # NEW: Recursion stack.
	while work:
		v, i = work.pop() # i is next successor to process.
		if i == 0: # When first visiting a vertex:
			ids[v] = next
			lowlink[v] = next
			next += 1
			stack.append(v)
			onstack[v] = True
		recurse = False
		for j in range(i, len(adj[v])):
			w = adj[v][j]
			if ids[w] == None:
				# CHANGED: Add w to recursion stack.
				work.append((v, j+1))
				work.append((w, 0))
				recurse = True
				break
			elif onstack[w]:
				lowlink[v] = min(lowlink[v], ids[w])
		if recurse: continue # NEW
		if ids[v] == lowlink[v]:
			com = []
			while True:
				w = stack.pop()
				onstack[w] = False
				com.append(w)
				groupid[w] = nextgroup
				if w == v: break
			groups.append(com)
			nextgroup += 1
		if work: # NEW: v was recursively visited.
			w = v
			v, _ = work[-1]
			lowlink[v] = min(lowlink[v], lowlink[w])

for v in range(N):
	if ids[v] == None:
		sconnect_iterative(v)

print(groups)