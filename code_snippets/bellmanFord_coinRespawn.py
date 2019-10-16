'''
problem url: https://atcoder.jp/contests/abc137/tasks/abc137_e
'''

# n, m, p = map(int, input().split())
 
# n, m, p = 4, 5, 10
# arr = [[1, 2, 1], [1, 4, 1], [3, 4, 1], [2, 2, 100], [3, 3, 100]]

# n, m, p = 2, 2, 10
# arr = [(1, 2, 100), (2, 2, 100)]

n, m, p = 3, 3, 10
arr = [(1, 2, 20), (2, 3, 30), (1, 3, 45)]

# n, m, p = 3, 4, 99999
# arr= [(1, 3, 8), (3, 2, 10), (2, 2, 100000), (2, 1, 3)]

abc = []
# edge = [[] for _ in range(n)]
rev_edge = [[] for _ in range(n)]
for i in range(m):
	a, b, c = arr[i]
	abc.append((a - 1, b - 1, p - c))
	# edge[a - 1].append(b - 1)
	rev_edge[b - 1].append(a - 1)
# print(rev_edge)

def dfs(e, s):
	v_set = {s}
	stack = [s]
	while stack:
		v = stack.pop()
		for next_v in e[v]:
			# print(next_v)
			if next_v in v_set:
				continue
			v_set.add(next_v)
			stack.append(next_v)
	return v_set

def bellman_ford(sub_abc, n):
	inf = float("inf")
	dist = [inf] * n
	dist[0] = 0
	for _ in range(n):
		updated = False
		for u, v, d in sub_abc:
			if dist[u] + d < dist[v]:
				dist[v] = dist[u] + d
				updated = True
		if not updated:
			break
	else:
		return -1
	return max(-dist[n - 1], 0)


use = dfs(rev_edge, n - 1)
print(bellman_ford([(a, b, c) for (a, b, c) in abc if a in use and b in use], n))