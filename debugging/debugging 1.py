# Untitled 3.py
# Created by Kids on 6/1/21.
# this function adds up the numbers in a list and returns "Input Error" if it cant
def recurse_for_me(list_of_numbers_to_add, sum_=0):
	try:
		if len(list_of_numbers_to_add) == 0:
			return sum_
		else:
			sum_ += list_of_numbers_to_add[0]
			return recurse_for_me(list_of_numbers_to_add[1:], sum_)
	except:
		return "Input Error"
def unitest_():
	testlist = [43, 33, 37, 37]
	answer = 150
	try:
		result = recurse_for_me(testlist)
	except:
		result = None
	if result == answer:
		print("Test_: Pass")
	else:
		print("Test_: Fail")
def unittest1():
	testlist = [4, 3, 17, 7]
	answer = 31
	try:
		result = recurse_for_me(testlist)
	except:
		result = None
	if result == answer:
		print("Test 1: Pass")
	else:
		print("Test 1: Fail")


def unittest2():
	testlist = [4, 3, -7]
	answer = 0
	try:
		result = recurse_for_me(testlist)
	except:
		result = None
	if result == answer:
		print("Test 2: Pass")
	else:
		print("Test 2: Fail")
		
def unittest3():
	testlist = [-1, -2, -3, -4]
	answer = -10
	try:
		result = recurse_for_me(testlist)
	except:
		result = None
	if result == answer:
		print("Test 3: Pass")
	else:
		print("Test 3: Fail")
		
		
def unittest4():
	testlist = []
	answer = 0
	try:
		result = recurse_for_me(testlist)
	except:
		result = None
	if result == answer:
		print("Test 4: Pass")
	else:
		print("Test 4: Fail")

def unittest5():
	testlist = ["hi", "bye"]
	answer = "Input Error"
	try:
		result = recurse_for_me(testlist)
	except:
		result = None
	if result == answer:
		print("Test 5: Pass")
	else:
		print("Test 5: Fail")
		
def unittest6():
	testlist = [4, -6, 8, 10]
	answer = 16
	try:
		result = recurse_for_me(testlist)
	except:
		result = None
	if result == answer:
		print("Test 6: Pass")
	else:
		print("Test 6: Fail")

def run_unittests():
	unittest1()
	unittest2()
	unittest3()
	unittest4()
	unittest5()
	unittest6()
	unitest_()
if __name__ == "__main__":
	run_unittests()