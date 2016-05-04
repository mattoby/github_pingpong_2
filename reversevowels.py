import unittest

## Reverse Vowels of a String ##
'''

## We will write a function that will take a string s and
## reverse only the vowels of a string

# Example 1:

# Input s = "hello"

# Expected output = "holle"

# Example 2:

# Input s = "leetcode"

# Expected output = "leotcede"

# here is a list of vowels in english language
'''

def split_vowels_and_consonants(s):
	'''
	creates a vowel and a consonant list from an initial string s
	indicator is an indicator of whether an index of s is a vowel.
	'''

	vowels = ['a','e','o','u','i']
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

	return s_vowels, s_consonants, indicator


def reverse_string(s):
	'''
	reverse a string
	'''
	# initialize a list to store reversed values
	s_reversed = ['0'] * len(s)

	# loop to reverse string
	for i in xrange(len(s)):
		s_reversed[i] = s[len(s)-1-i]

	return s_reversed


def merge_vowels_and_consonants(s_vowels, s_consonants, indicator):
	'''
	merges a vowel and a consonant list into positions in a new list, where 'indicator' indicates where the vowels should be. this is the reverse function of split_vowels_and_consonants.
	'''
	# initialize a list to store string with reversed vowels
	s = ['0'] * len(indicator)

	# loop over the indicator. If one get the string from vowels
	# if 0 get string from consonants. Modify vowels and consonants.

	for i in xrange(len(indicator)):

		if indicator[i] == 1:

			s[i] = s_vowels[0]
			s_vowels = s_vowels[1::]
		else:

			s[i] = s_consonants[0]
			s_consonants = s_consonants[1::]

	return s


def reverseVowels(s):

	# create strings to store consonants and vowels separately.
	s_vowels, s_consonants, indicator = split_vowels_and_consonants(s)

	# now reverse the vowels
	s_vowels = reverse_string(s_vowels)

	# Now we will put back the consonanats and reversed vowels
	s = merge_vowels_and_consonants(s_vowels, s_consonants, indicator)

	# Change the list into a string
	s = ''.join(s)

	# return the string whose vowels are reversed
	return s


### Tests:

class MyTest(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(reverseVowels('hello'), 'holle')
        self.assertEqual(reverseVowels('leetcode'), 'leotcede')
        self.assertEqual(reverseVowels('XaYeZiRoSu'),'XuYoZiReSa')

    def test_twowords(self):
        self.assertEqual(reverseVowels('hello world'),'hollo werld')

    def test_punctuation(self):
    	self.assertEqual(reverseVowels('hello! world!'),'hollo! werld!')

    def test_numbers(self):
    	self.assertEqual(reverseVowels('h3llo friend'),'h3lle friond')

if __name__=='__main__':
    unittest.main()






