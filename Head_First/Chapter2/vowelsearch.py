# Chapter 2, Page 61
# Learned input() function to allow user to enter data.
# However, captialization is an issue... Try the word "Eating."

vowels = [ 'a', 'e', 'i', 'o', 'u' ]
word = input("Provide a word to search for vowels: ")
found = []
for letter in word:
	if letter in vowels:
		if letter not in found:
			found.append(letter)
for vowel in found:
	print(vowel)
