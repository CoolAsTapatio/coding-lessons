import sys
#this code finds the b's in the a
def how_many_of(given_list, given_key):
	how_many_in = 0 #finds how many of the given number are in the given list
	for i in given_list:
		for t in str(i):
			if str(given_key) == t:
				print("yes")
				how_many_in += 1
	return how_many_in
		

def unittest1():
	print("unittest_1")
	a1 = [2, 5, 6, 1, 5, 43, 8, 55, 6, 15, 53]
	b1 = 5
	expected = 6
	try:
		answer = how_many_of(a1, b1)
		if answer == expected:
			print("Test 1: PASS")
		else:
			print("Test 1: FAIL")
	except Exception as e:
		print(e)
		print("ERROR")
		print("Test 1: FAIL")

def unittest2():
	print("unittest_2")
	a2 = []
	b2 = 4
	expected = 0
	try:
		answer = how_many_of(a2, b2)
		if answer == expected:
			print("Test 2: PASS")
		else:
			print("Test 2: FAIL")
	except:
		print("ERROR")
		print("Test 2: FAIL")
		
def unittest3():
	print("unittest_3")
	a3 = ["hi", "biii", "hello", "chai"]
	b3 = "i"
	expected = 5
	try:
		answer = how_many_of(a3, b3)
		if answer == expected:
			print("Test 3: PASS")
		else:
			print("Test 3: FAIL")
	except:
		print("ERROR")
		print("Test 3: FAIL")
		
def unittest4():
	print("unittest_4")
	a4 = [17, 9, 1, 26, 43, 44, 59, 97, 6, 49, 53]
	b4 = 8
	expected = 0
	try:
		answer = how_many_of(a4, b4)
		if answer == expected:
			print("Test 4: PASS")
		else:
			print("Test 4: FAIL")
	except:
		print("ERROR")
		print("Test 4: FAIL")

def adv_unittest1():
	print("unittest_adv")
	a_adv = ["yolo", "bruh", "cobra", "bear", "brown", "blacker"]
	b_adv = "br"
	expected = 3
	try:
		answer = how_many_of(a_adv, b_adv)
		if answer == expected:
			print("Adv Test 1: PASS")
		else:
			print("Adv Test 1: FAIL")
	except:
		print("ERROR")
		print("Adv Test 1: FAIL")

def run_unittests():
	unittest1()
	unittest2()
	unittest3()
	unittest4()
	adv_unittest1()

if __name__ == "__main__":
	run_unittests()