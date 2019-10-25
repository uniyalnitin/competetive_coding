'''
problem_url -: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/
editorial_links -: 1. Youtube -: https://www.youtube.com/watch?v=5lWJpTEnyow
2. leetcode discussion-: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/discuss/161651/Easy-Python-Recursive-Solution-with-Explanation

Idea: The first element in "pre" and the last element in "post" should both be the value of the root. The second to last of "post" 
		should be the value of right child of the root. So we can find the index to split "left" and "right" children in "pre".
		Don't forget to evaluate if the length of "post" is larger than 1, since we used post[-2].
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
		if not pre or not post:
			return None

		root = TreeNode(pre[0])
		if len(post)==1: return root 
		
		idx = pre.index(post[-2])
		root.left = self.constructFromPrePost(pre[1: idx], post[: idx - 1])
		root.right = self.constructFromPrePost(pre[idx:], post[idx-1: -1])
		
		return root