'''
This is a classic dynamic programming problem. We'll need to find minimal vertex cover of an unweighted, undirected tree.

We'll try to find the optimal solution for the subtree rooted at each node considering either its parent is 
covered (and as such the edge between it and its parent) or its parent is not covered. 
In the first case, we have the freedom to either cover the current node or not.
But in the second case, we must cover the current node. 
Optimal solution is the one that uses least nodes.
'''

from collections import defaultdict
n = 13
tree = {
	1 : [2, 3, 4, 5, 6, 7],
	2 : [1, 8, 9, 10, 11, 12, 13],
	3 : [1],
	4 : [1],
	5 : [1],
	6 : [1],
	7 : [1],
	8 : [2],
	9 : [2],
	10 : [2],
	11 : [2],
	12 : [2],
	13 : [2]
}

dp = defaultdict(lambda: defaultdict(lambda:int(-1)))

def v_cover(cur, parent, is_parent_covered):
	if dp[cur][is_parent_covered] != -1:
		return dp[cur][is_parent_covered]

	# Case 1 - parent is selected
	if is_parent_covered:
		ret = 0		# current node is not selected
		for vertex in tree[cur]:
			if vertex != parent:
				ret += v_cover(vertex, cur, False) # case 1.1 - Don't choose the current node, 
		r = 1	# current node is selected
		for vertex in tree[cur]:
			if vertex != parent:
				r += v_cover(vertex, cur, True) # case 1.2 - select the current node 

		dp[cur][is_parent_covered] = min(r, ret)
		return dp[cur][is_parent_covered]
	else:	# Case 2 - parent is not selected (hence current node is always selected)
		r = 1	# current node is not selected
		for vertex  in tree[cur]:
			if vertex != parent:
				r += v_cover(vertex, cur, True) # select the current node as its parent is not selected
		dp[cur][is_parent_covered] = r
		return r

r = 1	#case 1. parent is selected
for vertex in tree[1]:
	r += v_cover(vertex, 1, True)
ret = 0	# case 2. Parent is not selected
for vertex in tree[1]:
	ret += v_cover(vertex, 1, False)
print(min(r, ret))
