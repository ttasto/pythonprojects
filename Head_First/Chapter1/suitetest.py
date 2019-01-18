# Chapter 1, Page 18
# Practing using the datetime module in conjunction with their example of how
# suites work for conditionals. The isoweekday() function lists the day as 1-7.

import datetime

today = datetime.date.isoweekday(datetime.date.today())

if today == 6:
	print("Saturday, time to party!")
elif today == 7:
	condition = input("Today is Sunday, do you have a headache? (yes/no): ")
	if condition == 'yes':
		print("Recover, then rest.")
	else:
		print("Rest.")
else:
	print("Work, work, work.")
