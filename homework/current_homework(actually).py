# Untitled.py
# Created by Kids on 10/20/20.
def printer(list_all):
	for i in list5:
		for i2 in i:
			print(i2)
def charecter(char, list5):
	how_many = 0
	for i in list5:
		for i2 in i:
			for i3 in i2:
				if char == i3:
					how_many += 1
	return how_many
def name_(charecter_, list_all):
	for i in list5:
		for i2 in i:
			if charecter_ in i2:
				return i2 	
							
'''

1) Determine the runtime for your name_ function
2) Write a function that returns the name of the player with the nth instance of a character where n is a param and char is a param and the list of lists is a param
3) Calculate the runtime for this new function (remember to use variables to describe the WORST CASE (i.e. maximum number of characters or length of data structure etc.)

'''
if __name__ == "__main__":
	list1 = ["LeBron James", "Micheal Jordan", "Bill Russel", "Kobe Bryant", "Steph Curry",]
	list2 = ["Christiano Ronaldo", "Lionel Messi", "Neymar", "Pele", "Fer D'ppolito"]
	list3 = ["Willie Mays", "Mike Trout", "Javier Baez", "Lou Gerhig", "Chris Bryant"]
	list4 = ["Walter Payton", "Gale Sayers", "Bryan Urlocher", "Pat Mahomes"]
	list5 = [list1, list2, list3, list4]
	answer  = input("please give a letter in the alphabet\n")
	print(name_(answer, list5))