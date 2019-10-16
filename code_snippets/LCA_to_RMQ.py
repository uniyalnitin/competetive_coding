'''
reduce the LCA problem to RMQ in linear time, so every algorithm that solves the RMQ problem will solve the LCA problem too
'''
import queue
import math

tree = {1:[2, 3, 4], 
		2:[1],
		3:[1, 5, 6, 7],
		4:[1],
		5:[3],
		6:[3, 8, 9],
		7:[3, 10, 11],
		8:[6],
		9:[6],
		10:[7, 12, 13],
		11:[7],
		12:[10],
		13:[10]
		}
n = 13

ET = [] # the nodes visited in an Euler Tour of T; E[i] is the label of i-th visited node in the tour
level = [-1]*(n+1)

def euler_tree(src, pre_level):
	global level
	ET.append(src)
	level[src] = pre_level + 1
	for neighbour in tree.get(src, []):
		if level[neighbour] == -1:
			euler_tree(neighbour, pre_level+1)
			ET.append(src)

euler_tree(1, -1)

L = [level[x] for x in ET]	#the levels of the nodes visited in the Euler Tour; L[i] is the level of node E[i]
# print(L)
def get_H():
	H = [-1]*(n+1)
	visited = [False]*(n+1)
	for i in range(len(ET)):
		if not visited[ET[i]]:
			H[ET[i]] = i
			visited[ET[i]] = True
	return H 
H = get_H()	#H[i] is the index of the first occurrence of node i in E

u, v = 11, 12

if H[u] > H[v]: u, v = v, u

N = len(L)
# print(N)
M = [[0]*(int(math.log2(N))+1) for i in range(N+1)]

def pre_process(arr, N, M):

	for i in range(N):
		M[i][0] = i

	for j in range(1, int(math.log2(N))+1):
		i = 0
		while i + (1 << j) -1 < N:
			M[i][j] = M[i][j-1] if arr[M[i][j-1]] <= arr[M[i + (1 << (j-1))][j - 1]] else M[i + (1 << (j-1))][j-1]	# interval comparision
			i += 1

def rangeMinQuery(i, j):
	k = int(math.log2(j - i + 1))

	return M[i][k] if L[M[i][k]] <= L[M[j - (1 << k)][k]] else M[j - (1 << k)][k]

pre_process(L, N, M)
# print(M)
q = rangeMinQuery(H[u], H[v])	
print(ET[q]) #LCAT(u, v) = E[rangeMinQuery(L(H[u], H[v])]
print(ET) #LCAT(u, v) = E[rangeMinQuery(L(H[u], H[v])]