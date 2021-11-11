# Untitled.py
# Created by Kids on 6/29/21.
class Obj:
	def __init__(self, first_phrase, second_phrase, _third_phrase):
		self.i = first_phrase
		self.a = second_phrase
		self.b = _third_phrase
	def get_i(self):
		print("hi")
		return self.i
	def get_a(self):
		print("hii")
		return self.a
	def get_b():
		print("hiii")
		return self.b
	
def operate_on_two_from_obj(object_, operation, first_value, second_value):
	if first_value == 'i':
		first = object_.i
	if first_value == 'a':
		first = object_.a
	if first_value == 'b':
		first = object_.b
	if second_value == 'i':
		second = object_.i
	if second_value == 'a':
		second = object_.a
	if second_value == 'b':
		second = object_.b
	
	if operation == "add":
		return first + second
	elif operation == "sub":
		return first - second
	elif operation == "mul":
		return first * second
	elif operation == "div":
		if second == 0:
				return "Error"
		else:
			return first / second
	else:
		return "Error"

def unittest1():
	try:
		print("starting try")
		obj_iab_148 = Obj(1, 4, 8)
		print("object complete")
		result = operate_on_two_from_obj(obj_iab_148, "add", 'i', 'a')
		print("result found")
		expected = 5
		if result == expected:
			print("Test 1: PASS")
		else:
			print("Test 1: FAIL")
	except:
		print("unitest_ 1")
		print("Test 1: FAIL")

def unittest2():
	try:
		obj_iab_726 = Obj(7, 2, 6)
		result = operate_on_two_from_obj(obj_iab_726, "sub", 'a', 'b')
		expected = -4
		if result == expected:
			print("Test 2: PASS")
		else:
			print("Test 2: FAIL")
	except:
		print("Test 2: FAIL")

def unittest3():
	try:
		obj_iab_162 = Obj(1, 6, 2)
		result = operate_on_two_from_obj(obj_iab_162, "mul", 'a', 'a')
		expected = 36
		if result == expected:
			print("Test 3: PASS")
		else:
			print("Test 3: FAIL")
	except:
		print("Test 3: FAIL")

def unittest4():
	try:
		obj_iab_534 = Obj(5, 3, 4)
		result = operate_on_two_from_obj(obj_iab_534, "div", 'i', 'b')
		expected = 1.25
		if result == expected:
			print("Test 4: PASS")
		else:
			print("Test 4: FAIL")
	except:
		print("Test 4: FAIL")

def unittest5():
	try:
		obj_iab_041 = Obj(0, 4, 1)
		result = operate_on_two_from_obj(obj_iab_041, "div", 'a', 'i')
		expected = "Error"
		if result == expected:
			print("Test 5: PASS")
		else:
			print("Test 5: FAIL")
	except:
		print("Test 5: FAIL")
		
def unittest6():
	try:
		obj_iab_123 = Obj(1, 2, 3)
		result = operate_on_two_from_obj(obj_iab_123, "hi", 'a', 'i')
		expected = "Error"
		if result == expected:
			print("custom test 6: PASS")
		else:
			print("custom test 6: FAIL")
	except:
		print("Custom Test 6: FAIL")
def unittest7():
	# write me another unittest case you can think of
	print("Custom Test 7: FAIL")
	
def run_unittests():
	unittest1()
	unittest2()
	unittest3()
	unittest4()
	unittest5()
	unittest6()
	unittest7()
	
if __name__ == "__main__":
	run_unittests()	