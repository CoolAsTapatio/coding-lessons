	
def add8plus6():
	d = 8 + 6
	print("hi")
	return d
def add9plus27():
	print("how are you")
	v = 9 + 27
	return v
def add10plus10():
	de = 10 + 10
	print("bye")
	return de
def funcall():
	f = add10plus10()
	t = add8plus6()
	g = add9plus27()
	print("haha")
	return 14 / 7
def thefunction():
	answer = int(input("please submit a number\n"))
	answer2 = int(input("please submit another number\n"))
	total = answer + answer2
	return total	
	
# New Concept: Parameters!!
# Parameters are variables you pass into a function --> pass in means put in between the paranthesis. Those values can be used inside the function

def add(num1, num2):
	#print(num1)
	#print("num1 is equal to " + str(num1))
	#print("num2 is equal to " + str(num2))
	total = num1 + num2
	return total
def calcofthetotal(aglis):
	mySum = 0
	for i in aglis:
		mySum = mySum + i
	return mySum
	
def calcTotalAge(ageList):
	mySum1 = 0
	for i in ageList:
		mySum1 = add(mySum1, i)
	return mySum1
if __name__ == "__main__":
	#print(thefunction())
	#print(num1)
	v = add(17, 249)
	agesoffam = [11, 8, 46, 47]
	e = calcofthetotal(agesoffam)
	print(e)
	m = calcTotalAge(agesoffam)
	print(m)
	