
stdin = open("testdata.txt")
def input():
	return stdin.readline().strip()

'''
problem url: https://leetcode.com/problems/distribute-coins-in-binary-tree/
editorial url: https://massivealgorithms.blogspot.com/2019/02/leetcode-979-distribute-coins-in-binary.html
'''

class TreeNode:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

class Solution:

	def traverse(self, root):
		if not root:
			return 0
		left = self.traverse(root.left)
		right = self.traverse(root.right)
		self.moves += abs(left) + abs(right)
		return left + right + root.val - 1

	def distributeCoins(self, root):
		self.moves = 0
		self.traverse(root)
		return self.moves

tree = [0, 3, 0]
root = TreeNode(tree[0])
root.left = TreeNode(tree[1])
root.right = TreeNode(tree[2])

sol = Solution()
ans = sol.distributeCoins(root)
print(ans)