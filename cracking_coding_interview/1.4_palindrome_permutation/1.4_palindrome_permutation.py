def str_to_i(letter: str)->int:
	return ord(letter)-ord('a')

def palindromePermutation(str1: str)->str:
	occurrences = [0]*27

	for letter in str1:
		i = str_to_i(letter)
		occurrences[i]+=1

	# if all occurrences are divisible by 2
	# and there is 1 with remaining 1

	divs = list(map(lambda x: x%2, occurrences))
	if len(str1)%2 == 0:
		return True if set(divs) == {0} else False
	else:
		ones = [True if elem==1 else False for elem in divs]
		return True if sum(ones)==1 else False

if __name__ == '__main__':
	word = 'abccba'
	print("is the word '{}' permutation of palindromic? {}".format(word, palindromePermutation(word)))


	word = 'aabbccdd'
	print("is the word '{}' permutation of palindromic? {}".format(word, palindromePermutation(word)))


	word = 'abccdd'
	print("is the word '{}' permutation of palindromic? {}".format(word, palindromePermutation(word)))

	word = 'aabbccd'
	print("is the word '{}' permutation of palindromic? {}".format(word, palindromePermutation(word)))
