'''
Problem url-: https://leetcode.com/problems/delete-nodes-and-return-forest/
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
			
	def delNodes(self, root, to_delete):
		"""
		:type root: TreeNode
		:type to_delete: List[int]
		:rtype: List[TreeNode]
		"""
		td = set(to_delete)
		ans = []
		
		def delete(parent, s, root):
			if not root:
				return
			if root.val in td:
				if parent:
					if s=="left":
						parent.left = None
					else:
						parent.right = None
				delete(None, "left", root.left)
				delete(None, "right", root.right)
			else:
				if not parent:
					ans.append(root)
				delete(root, "left", root.left)
				delete(root, "right", root.right)
				
		delete(None, "", root)
		return ans