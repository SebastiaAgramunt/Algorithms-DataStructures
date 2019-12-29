from trie import Node
from trie import Trie
from trie import longestCommonSubstring

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


	word1 = 'abcxxyzkkllmzb'
	word2 = 'cxxyzkfasdfkkllmabcxxz'

	print('Longest common substring of {} and {} is {}'.format(word1, word2, longestCommonSubstring(word1, word2)))