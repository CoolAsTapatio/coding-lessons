# Untitled.py
# Created by Kids on 9/8/20.

'''listofgrades = ["1st", "2nd", "3rd", "4th", "5th", "6th"]
whatgrade = 1
while whatgrade < 6:
	print("wait " + str(6 - whatgrade) + " more years.")
	whatgrade = whatgrade + 1
	if whatgrade == 6:
		print(str(listofgrades[5]) + " is the best grade.")'''
'''age = 11
unchange = 16
drive = False
while drive == False:
	if age == unchange:
		drive = True
	else:
		drive = False
	if drive == False:
		print("you are " + str(unchange - age) + " years too young to drive.")
	else:
		print("you can drive.")
	age = age + 1'''
listoffivestates = ["New York", "New Jersey", "Hawaii", "Alabama", "Idaho", "indiana", "Alaska"]
for i in listoffivestates:
	if i == listoffivestates[0] or i == listoffivestates[6]:
		print(str(i) + " is the best state")
	else:
		print("I hate " + str(i))