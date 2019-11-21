#build level graph by using BFS
def Bfs(C, F, s, t):  # C is the capacity matrix
	global level
	n = len(C)
	queue = []
	queue.append(s)
	level = n * [0]  # initialization
	level[s] = 1  
	while queue:
		k = queue.pop(0)
		for i in range(n):
				if (F[k][i] < C[k][i]) and (level[i] == 0): # not visited
						level[i] = level[k] + 1
						queue.append(i)
	return level[t] > 0

#search augmenting path by using DFS
def Dfs(C, F, k, cap):
	if k == len(C)-1:
		return cap
	for i in range(len(C)):
		if (level[i] == level[k] + 1) and (F[k][i] < C[k][i]):
			bottleneck = Dfs(C,F,i,min(cap,C[k][i] - F[k][i]))
			if bottleneck > 0:
				F[k][i] = F[k][i] + bottleneck
				F[i][k] = F[i][k] - bottleneck
				return bottleneck
	return 0

#calculate max flow
#_ = float('inf')
def MaxFlow(C,s,t):
	n = len(C)
	F = [n*[0] for i in range(n)] # F is the flow matrix
	max_flow = 0
	while(Bfs(C,F,s,t)):
		add = Dfs(C,F,s,100000)
		max_flow += add
		while add:
			add = Dfs(C,F,s,100000)
			max_flow += add
	return max_flow

#-------------------------------------
# make a capacity graph
# node   s   o   p   q   r   t
C = [[ 0, 10, 0, 8, 0, 0 ],  # s
	 [ 0, 0, 5, 2, 0, 0 ],  # o
	 [ 0, 0, 0, 0, 0, 7 ],  # p
	 [ 0, 0, 0, 0, 10, 0 ],  # q
	 [ 0, 0, 8, 0, 0, 10],  # r
	 [ 0, 0, 0, 0, 0, 0]]  # t

source = 0  # A
sink = 5    # F
print("Dinic's Algorithm")
max_flow_value = MaxFlow(C, source, sink)
print("max_flow_value is", max_flow_value)