'''
problem statement-: find the longest word in words that can be built one character at a time by other words in words. 
		If there is more than one possible answer, return the longest word with the smallest lexicographical order.
'''
from collections import defaultdict, deque

words =  ["w","wo","wor","worl", "world"]

class TrieNode:
	def __init__(self):
		self.children = defaultdict(TrieNode)
		self.isEnd = False
		self.word = ''


class Trie:
	def __init__(self):
		self.root = TrieNode()

	def insert(self, word):
		current = self.root
		for letter in word:
			current = current.children[letter]
		current.isEnd = True
		current.word = word 

	def search(self, word):
		current = self.root
		for letter in word:
			current = current.children.get(letter)
			if current is None:
				return False
		return current.isEnd

	def starts_with(self, prefix):
		current = self.root
		for letter in prefix:
			current = current.children.get(letter)
			if current is None:
				return False
		return True

	def bfs(self):
		q = deque([self.root])
		res = ''
		while q:
			cur = q.popleft()
			for n in cur.children.values():
				if n.isEnd:
					q.append(n)
					if len(n.word) > len(res) or n.word < res:
						res = n.word 
		return res


trie = Trie()
for word in words:
	trie.insert(word)
ans = trie.bfs()
print(ans)