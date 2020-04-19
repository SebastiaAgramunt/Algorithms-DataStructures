
class Node:
	def __init__(self):
		# children is a container of Nodes, initialized as None
		self.children = [None]*26
		# Deternines if the current Node is end of world
		self.endOfWord = False
		# Times we passed though this node storing one letter
		self.n = 0

class Trie:
	def __init__(self):
		self.root = Node()

	def _charToIdx(self, ch):
		# Return from 0 to 26. Letters
		return ord(ch) - ord('a')

	def insert(self, word):
		# Insert the word if not exists
		nodeCrawler = self.root
		for letter in word:
			idx = self._charToIdx(letter)
			if nodeCrawler.children[idx] is None:
				nodeCrawler.children[idx] = Node()

			nodeCrawler = nodeCrawler.children[idx]
			nodeCrawler.n+=1

		nodeCrawler.endOfWord = True

	def search(self, word):
		# search for a word
		nodeCrawler = self.root

		for letter in word:
			idx = self._charToIdx(letter)
			if nodeCrawler.children[idx] is None:
				return False
			nodeCrawler = nodeCrawler.children[idx]

		return nodeCrawler.endOfWord

	def search_depth(self, substr):
		# search if this substring is in any word
		nodeCrawler = self.root

		max_substr = ''
		for letter in substr:
			idx = self._charToIdx(letter)
			if nodeCrawler.children[idx] is None:
				return max_substr
			else:
				max_substr+=letter
			nodeCrawler = nodeCrawler.children[idx]
		return max_substr


def longestCommonSubstring(str1: str, str2: str):
	# Build a trie of substrings of the first word
	trie = Trie()
	for i in range(0, len(str1)):
		#print(str1[i:])
		trie.insert(str1[i:])

	substr = ''
	for i in range(0, len(str2)):
		max_substr = trie.search_depth(str2[i:])
		if len(max_substr) > len(substr):
			substr = max_substr

	return substr
