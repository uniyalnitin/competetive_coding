'''
 if L[p] != L[q]. Assume, without loss of generality, that L[p] < L[q].
  We can use the same meta-binary search for finding the ancestor of p situated on the same level with q, 
 and then we can compute the LCA as described below
'''

import math
import queue

tree = {1:[2, 3, 4], 
		3:[5, 6, 7],
		6:[8, 9],
		7:[10, 11],
		10:[12, 13]
		}
n = 13

level = [-1]*(n+1)

#T[i] => parent of ith node
T = [-1]*(n+1)

def bfs(src):
	level[src] = 0
	que = queue.Queue()


	que.put(src)

	while not que.empty():
		v = que.get()

		for neighbour in tree.get(v, []):
			que.put(neighbour)
			level[neighbour] = level[v] + 1
			T[neighbour] = v

bfs(1)

#P[i][j] = 2^jth ancestor of i
P = [[-1]*(int(math.log2(n))+1) for i in range(n+1)]

def process(n, tree, P):
	'''
	recurrance: P[i][j] = Tree[i] if j==0 else P[P[i][j-1]][j-1]
	'''
	for i in range(1, n+1):
		P[i][0] = T[i]	# T[i] => parent of i

	# print(P)
	for j in range(1, int(math.log2(n))+1):
		for i in range(n+1):
			if P[i][j-1] != -1:
				P[i][j] = P[P[i][j-1]][j-1]

def lca_query(p, q):
	if level[p] < level[q]:		# if p is situated on a higher level than q then swap them
		p, q = q, p
	# print(p, level[p])
	# log = 1
	log = int(math.log2(level[p]))
	# while (1 << log) <= level[p]:
	# 	log += 1
	# log -= 1

	# find the ancestor of p situated on same level with q using values in P
	for i in range(log, -1, -1):
		if level[p] - (1 << i) >= level[q]:
			p = P[p][i]
	if p==q:
		return p

	for i in range(log, -1, -1):
		if P[p][i] != -1 and P[p][i] != P[q][i]:
			p = P[p][i]
			q = P[q][i]
			
	return P[p][0]


process(n, tree, P)
# print(P)
# print(level)
q = lca_query(9, 12)
print(q)