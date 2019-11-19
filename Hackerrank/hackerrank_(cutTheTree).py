'''
	Problem Url: https://www.hackerrank.com/challenges/cut-the-tree/problem
	Idea: run DFS or BFS to get the cumulative sum of subtree for each node.
'''

from collections import deque

class Node(object):
	def __init__(self,index,value):
		self.index = index
		self.value = value
		self.children = set()
		self.parent = None
		self.value_of_subtree = 0

N = int(input())
node_at_index = [Node(index,value) for index,value in enumerate(map(int,input().split()))]
for a, b in (map(int,input().split()) for _ in range(N-1)):
	node_at_index[a-1].children.add(node_at_index[b-1])
	node_at_index[b-1].children.add(node_at_index[a-1])

root = node_at_index[0]
ordered_nodes = [root]
q = deque([root])
while q:
	n = q.popleft()
	for c in n.children:
		c.children.remove(n)
		c.parent = n
		q.append(c)
		ordered_nodes.append(c)
ordered_nodes.reverse()
'at this point, ordered_nodes are ordered from leaf to root'
		
for n in ordered_nodes:
	n.value_of_subtree = n.value + sum(c.value_of_subtree for c in n.children)
	
total = root.value_of_subtree
best = N * 2000
for n in ordered_nodes:
	for c in n.children:
		tree_a = c.value_of_subtree
		tree_b = total - tree_a
		dif = abs(tree_a - tree_b)
		if dif < best:
			best = dif
			
print(best)