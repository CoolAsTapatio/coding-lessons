# Untitled.py
# Created by Kids on 9/5/20.

'''listoftvshows = ["the flash", "arrow", "supergirl", "legends of tommorow", "stargirl"]
for i in listoftvshows:
	print(i + "\n")
listofbooks = ["harry potter and the sorcerer's stone", "percy jackson and the sea of monsters", "the ring of sky"]
listofauthorsofthecorrespondingbooks = ["jk rowling", "rick riordan", "chris bradford"]
for t in range(0, len(listofbooks), 1):
	print(listofbooks[t] + " is written by " + listofauthorsofthecorrespondingbooks[t])'''
listofnames = ["theo", "xander", "matt", "grant", "rob"]
#answer = input("give me a name so that I can index it please. \n")
#for a in range(0, len(listofnames), 1):
	#if answer == listofnames[a]:
		#print(a)
"""magicnumber = 8
answer = int(input("how old is your kid\n"))
if answer == 8:
	print("welcome to the palace of eight")
elif answer >= 9:
	print("you are " + str(answer - 8) + " years to old. come back again last year.")
else:
	print("your are " + str(8 - answer) + " years too young. come back again next year.")"""
doesthestorehavecheeseits = True
answer = input("do you have your parents permission?\n")
d = 1
while doesthestorehavecheeseits and answer == "yes" and d < 1:
	print("you are not old enough")
	d = d +1