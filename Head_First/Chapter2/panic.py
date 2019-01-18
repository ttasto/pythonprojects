# Chapter 2, Pages 67-68
# Practice with lists: turn str "Don't panic!" into str "on tap"

phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)

# My solution:

plist.pop(0)		# Removes "D"
for items in range(9):	# Removes all list items except 'o' and 'n'
	plist.pop(2)
plist.extend([' ', 't', 'a', 'p'])

# Head First solution:

#for i in range(4):	# Removes 'n', 'i', 'c', '!'
# 	plist.pop()
#plist.pop(0)		# Removes "D"
#plist.remove("'")	# Removes "'"
#plist.extend([plist.pop(), plist.pop()])	# Read as plist.extend([plist.pop()/'a', plist.pop()/'p'])
#plist.insert(2, plist.pop(3))			# Moves ' ' ahead of 't' in the list

new_phrase = ''.join(plist)
print(plist)
print(new_phrase)
