'''
	Problem Url: https://www.hackerrank.com/challenges/gena/problem
	Idea: Use BFS to get the minimum depth from current state to final state
'''

from collections import deque

def legal_moves(x):
	'''
		This function is used to get the valid moves from current state
	'''
	for i in range(len(x)):
		if x[i]:
			for j in range(len(x)):
				if not x[j] or x[i][-1] < x[j][-1]:
					# we can move disk from i to j iff either there is not disk at pole j or 
					# radius of top disk on pole j is greater that the ith pole top disk
					yield (i, j)

def is_goal(x):
	return all(len(x[i])==0 for i in range(1, len(x)))

def bfs(x):
	def tuplify(x):
		# convert list to tuple
		return tuple(tuple(ele) for ele in x)
	
	def do_move(state, m):
		y = [list(t) for t in state]
		y[m[1]].append(y[m[0]].pop())
		y[1:4] = sorted(y[1:4], key = lambda t: t[-1] if t else 0)
		return tuplify(y)
	
	visited = set()
	q = deque()

	start = (tuplify(x), 0)
	q.append(start)

	while q:
		state, depth = q.popleft()
		if is_goal(state):
			return depth
		for move in legal_moves(state):
			child_state = do_move(state, move)	# get the next valid state
			if child_state not in visited:
				visited.add(child_state)
				q.append((child_state, depth+1))

n = int(input())
R = list(map(int, input().split()))

A = [[] for _ in range(4)]

for i in range(n):
	A[R[i]-1] = [(i+1)] + A[R[i]-1]

print(bfs(A))
		