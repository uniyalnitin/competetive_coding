from queue import Queue

def bipartiteUtil(src):
	global graph, n, colorArr
	
	queue = Queue(maxsize=n*n)
	queue.put(src)
	
	while not queue.empty():
		u = queue.get()
		
		if graph[u][u]==1:	# if self loop
			return False
		
		for v in range(n):
			if graph[u][v] == 1 and colorArr[v]==-1:
				colorArr[v] = 0 if colorArr[u]==1 else 1
				queue.put(v)
			elif graph[u][v]==1 and colorArr[v]==colorArr[u]:
				return False
	return True

def isBipartite():
	global graph, n, colorArr
	
	for u in range(n):
		if colorArr[u] ==-1:
			if not bipartiteUtil(u):
				return False
	return True

graph = [[0, 1, 1],
		[1, 0, 1],
		[1, 1, 0]]

n = 3
colorArr = [-1 for i in range(n)]
ans = isBipartite()
print(ans)
# 062 51000 3843