

## Reverse Vowels of a String ## 


## We will write a function that will take a string s and
## reverse only the vowels of a string


# Example 1:

# Input s = "hello"

# Expected output = "holle"

# Example 2:

# Input s = "leetcode"

# Expected output = "leotcede"


# here is a list of vowels in english language
vowels = ['a','e','o','u','i']


def reverseVowels(s):

	# create strings to store consonants and vowels separately.
	s_consonants = ''
	s_vowels = ''
	# indicator function keeps track of the indices for vowels 
	# and consonants in the original string. 1 -> vowel, 0-> consonant
	indicator = [0] * len(s)
	for i in xrange(len(s)):

		if s[i] in vowels:
			
			s_vowels = s_vowels + s[i]
			indicator[i] = 1
		else:

			s_consonants = s_consonants + s[i]

	# now we seperated vowels from consonants we will reverse the vowels
	
	# initialize a list to store reversed vowels
	vowel_reversed = ['0'] * len(s_vowels)

	# loop to reverse vowels
	for i in xrange(len(s_vowels)):

		vowel_reversed[i] = s_vowels[len(s_vowels)-1-i]

	# Now we will put back the consonanats and reversed vowels
	
	# initialize a list to store string with reversed vowels
	reversed_s = ['a'] * len(s)


	# loop over the indicator. If one get the string from vowels 
	# if 0 get string from consonants. Modify vowels and consonants.

	for i in xrange(len(s)):

		if indicator[i] == 1:

			reversed_s[i] = vowel_reversed[0]
			vowel_reversed = vowel_reversed[1::]
		else:

			reversed_s[i] = s_consonants[0]
			s_consonants = s_consonants[1::]

	# Now we have the reversed string in a list 
	# All we need to do is change the list into a string 

	# initialize empty string
	reversed = ''

	# fill it from the list we created called reversed_s
	for s in reversed_s:
		reversed = reversed + s

	# print the  string whose vowels are reversed
	print reversed

reverseVowels('hello')

reverseVowels('leetcode')













