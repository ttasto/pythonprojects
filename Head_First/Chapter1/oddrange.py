# Chapter 1, Page 42
# After learning the range() function, I replaced the odds list with a listed range of odds.

from datetime import datetime

odds = list(range(1, 61, 2))

right_this_minute = datetime.today().minute

if right_this_minute in odds:
	print("This minute seems a little odd.")
else:
	print("Not an odd minute.")
