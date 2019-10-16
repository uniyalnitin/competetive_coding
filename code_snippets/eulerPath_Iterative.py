import sys
from collections import defaultdict

stdin = open("testdata.txt", "r")

def printCircuit(adjl):
	edge_count = defaultdict(int) # number of vertex emerging from a vertex
	for k in adjl:
		edge_count[k] = len(adjl[k])

	cur_v = 0
	cur_path = [cur_v]	#current_vert
	circuit = []

	while cur_path:
		if edge_count[cur_v]:
			cur_path.append(cur_v)
			edge_count[cur_v] -= 1
			next_v = adjl[cur_v].pop()
			cur_v = next_v
		else:
			circuit.append(cur_v)
			cur_v = cur_path.pop()
	for el in reversed(circuit):
		print(el, end="->")
	print()


class Graph(object):
	"""docstring for Graph"""
	def __init__(self, vertices):
		self.vertices = vertices
		self.graph = defaultdict(list)

	def add_edge(self,a,b):
		self.graph[a].append(b)
		self.graph[b].append(a)

	def eulerPath(self):
		g = self.graph
		odd = [k for k, v  in g.items() if len(v)%2 == 1]
		if len(odd) == 0 :
			odd = [list(g.keys())[0]]
		elif len(odd) == 1 or len(odd) > 2 :
			return None
		path = []
		stack = [odd[-1]]
		while stack:
			u = stack[-1]
			if g[u]:
				v = g[u][0]
				del g[u][0]
				del g[v][g[v].index(u)]
				stack.append(v)
			else:
				path.append(stack.pop())
		return path

n, e = map(int, stdin.readline().strip().split())
g = Graph(n)

u = []
v = []

for i in range(e):
	a, b = map(int, stdin.readline().strip().split())
	g.add_edge(a,b)
	u.append(a)
	v.append(b)
	
ans = g.eulerPath()

if ans is None:
	print('NO')
else:
	if len(ans) == (e+1) and ans[0] == ans[-1]:
		print("YES")
		temp = defaultdict(defaultdict)
		for i in range(len(ans)-1, 0, -1):
			temp[ans[i]][ans[i - 1]] = True
		for i in range(e):
			if u[i] in temp and v[i] in temp[u[i]]:
				print(u[i], v[i])
			else:
				print(v[i], u[i]) 		
	else:
		print("NO")