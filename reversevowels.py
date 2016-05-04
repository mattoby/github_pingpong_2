

## Reverse Vowels of a String ## 


## We will write a function that will take a string s and
## reverse only the vowels of a string


# Example 1:

# Input s = "hello"

# Expected output = "holle"

# Example 2:

# Input s = "leetcode"

# Expected output = "leotcede"



vowels = ['a','e','o','u','i']


def reverseVowels(s):
	s_consonants = ''
	s_vowels = ''
	indicator = [0] * len(s)
	for i in xrange(len(s)):

		if s[i] in vowels:
			
			s_vowels = s_vowels + s[i]
			indicator[i] = 1
		else:

			s_consonants = s_consonants + s[i]

	vowel_reversed = ['0'] * len(s_vowels)

	for i in xrange(len(s_vowels)):

		vowel_reversed[i] = s_vowels[len(s_vowels)-1-i]

	reversed_s = ['a'] * len(s)

	for i in xrange(len(s)):

		if indicator[i] == 1:

			reversed_s[i] = vowel_reversed[0]
			vowel_reversed = vowel_reversed[1::]
		else:

			reversed_s[i] = s_consonants[0]
			s_consonants = s_consonants[1::]

	reversed = ''
	for s in reversed_s:
		reversed = reversed + s

	print reversed

reverseVowels('hello')

reverseVowels('leetcode')













