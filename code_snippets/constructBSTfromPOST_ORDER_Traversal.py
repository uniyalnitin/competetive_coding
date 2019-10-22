INT_MIN = -2**31
INT_MAX = 2**31

class newNode: 
	def __init__(self, data): 
		self.data = data 
		self.left = self.right = None

def constructTreeUtil(key, min, max):
	global postIndex, post, size

	# Base case 
	if (postIndex < 0): 
		return None
	root = None

	if (key > min and key < max) :  
		root = newNode(key) 
		postIndex = postIndex - 1

		if (postIndex >= 0) : 
			root.right = constructTreeUtil(post[postIndex], key, max) 
			root.left = constructTreeUtil(post[postIndex], min, key) 
	return root 

def constructTree () : 
	global postIndex, post
	return constructTreeUtil(post[postIndex], INT_MIN, INT_MAX) 

def printInorder (node) : 

	if (node == None) : 
		return
	printInorder(node.left) 
	print(node.data, end = " ") 
	printInorder(node.right) 

post = [1, 7, 5, 50, 40, 10] 
size = len(post) 
postIndex = size-1 

root = constructTree() 

print("Inorder traversal of the", 
			"constructed tree: ") 
printInorder(root) 
