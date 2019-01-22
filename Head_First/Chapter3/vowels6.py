# Chapter 3, Page 130
# Using sets to modify program. 

vowels = set('aeiou')
word = input("Provide a word to search for vowels: ")
i = vowels.intersection(set(word)) # the book uses 'found' to find intersection of the two sets
for vowel in i:
	print(vowel)
