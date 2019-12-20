
class Node:
	def __init__(self):
		# children is a container of Nodes, initialized as None
		self.children = [None]*26
		# Deternines if the current Node is end of world
		self.endOfWord = False

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




if __name__ == '__main__':
	words = ['there', 'their', 'answer', 'any', 'bye']

	trie = Trie()
	for word in words:
		trie.insert(word)


	word = 'ther'
	print('Does the word {} appear in the Trie? {}'.format(word, trie.search(word)))

	word = 'there'
	print('Does the word {} appear in the Trie? {}'.format(word, trie.search(word)))

	word = 'bye'
	print('Does the word {} appear in the Trie? {}'.format(word, trie.search(word)))

	word = 'answer'
	print('Does the word {} appear in the Trie? {}'.format(word, trie.search(word)))

	word = 'an'
	print('Does the word {} appear in the Trie? {}'.format(word, trie.search(word)))