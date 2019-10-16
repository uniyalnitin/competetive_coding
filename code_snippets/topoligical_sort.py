import queue

adj_list = [[0]*6 for i in range(6)]
adj_list[0][1] = 1
adj_list[0][1] = 1
adj_list[1][2] = 1
adj_list[1][3] = 1
adj_list[2][3] = 1
adj_list[2][4] = 1
adj_list[2][5] = 1
adj_list[3][4] = 1
adj_list[3][5] = 1
adj_list[4][5] = 1

def topological_sort(n, adj):
	T = []
	visited = [0]*n
	in_degree = [0]*n
	que = queue.Queue()

	for i in range(n):
		for j in range(n):
			if adj[i][j]:
				in_degree[j] = in_degree[j] + 1

	for i in range(n):
		if in_degree[i]==0:
			que.put(i)
			visited[i] = True

	while not que.empty():
		vertex = que.get()
		T.append(vertex)
		for j in range(n):
			if adj[vertex][j] and (not visited[j]):
				in_degree[j] = in_degree[j] - 1
				if in_degree[j]==0:
					que.put(j)
					visited[j] = True
	return T

ans = topological_sort(6, adj_list)
print(ans)

T = []
visited = [0]*6
def topological_sortDFS(cur_vert, n, adj_list):
	global T, visited
	visited[cur_vert] = True

	for i in range(n):
		if adj_list[cur_vert][i] and not visited[i]:
			topological_sortDFS(i, n, adj_list)
	T.append(cur_vert)

topological_sortDFS(0, 6, adj_list)
print(T[::-1])