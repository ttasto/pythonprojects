# Chapter 2, Page 81
# Practice with lists: turn str "Don't panic!" into str "on tap" using list slice notation.

phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)

# My solution:

plist.remove("'")
plist.insert(3, plist.pop(4))
plist.insert(5, plist.pop(6))
new_phrase = ''.join(plist[1:7])

#Head First solution:

#new_phrase = ''.join(plist[1:3])
#new_phrase = new_phrase + ''.join([plist[5], plist[4], plist[7], plist[6]])

print(plist)
print(new_phrase)
