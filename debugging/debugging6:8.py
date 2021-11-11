
def hash_add(a, b, c):
	try:
		shirtprice_ = {"shirt1": 2, "shirt2" : 54, "shirt3" : 74.5}
		first_shirt = a
		second_shirt = b
		third_shirt = c
		price1 = price_lookup("shirt1", shirtprice_) * first_shirt
		price2 = price_lookup("shirt2", shirtprice_) * second_shirt
		price3 = price_lookup("shirt3", shirtprice_) * third_shirt
		return price1 + price2 + price3
	except:
		return "Error"
def price_lookup(x, shirtprice_):
	return shirtprice_[x]
def unittest1():
	try:
		shirt1 = 2
		shirt2 = 1
		shirt3 = 0
		answer = 58
		result = hash_add(shirt1, shirt2, shirt3)
		if answer == result:
			print("TEST1: PASS")
		else:
			print("TEST1: FAIL")
	except Exception as e:
		print(e)
		print("fail")
		print("TEST1: FAIL")	
def unittest2():
	try:
		shirt1 = 0
		shirt2 = 0
		shirt3 = 0
		answer = 0
		result = hash_add(shirt1, shirt2, shirt3)
		if answer == result:
			print("TEST2: PASS")
		else:
			print("TEST2: FAIL")
	except Exception as e:
		print(e)
		print("fail")
		print("TEST2: FAIL")

def unittest3():
	try:
		shirt1 = 0
		shirt2 = 1
		shirt3 = 2
		answer = 203
		result = hash_add(shirt1, shirt2, shirt3)
		if answer == result:
			print("TEST3: PASS")
		else:
			print("TEST3: FAIL")
	except Exception as e:
		print(e)
		print("fail")
		print("TEST3: FAIL")

def unittest4():
	try:
		shirt1 = "a"
		shirt2 = "2"
		shirt3 = "3"
		answer = "Error"
		result = hash_add(shirt1, shirt2, shirt3)
		if answer == result:
			print("TEST4: PASS")
		else:
			print("TEST4: FAIL")
	except Exception as e:
		print(e)
		print("fail")
		print("TEST4: FAIL")

def run_unittests():
	unittest1()
	unittest2()
	unittest3()
	unittest4()

if __name__ == "__main__":
	run_unittests()