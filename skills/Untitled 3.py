def is_in_a_row(mylist):
	increments = []
	for i in range(0, len(mylist)-1):
		if mylist[i] + 1 == mylist[i+1]:
			increments.append("Y")
		else:
			increments.append("n")
	if "n" in increments:
		return False
	else:
		return True

		
def unittest1():
	test_list = [2, 3, 4, 5, 7]
	answer = False
	if is_in_a_row(test_list) == answer:
		print("1: Pass")
	else:
		print("1: Fail")
		
def unittest2():
	test_list = [3, 4, 5, 6]
	answer = True
	try:
		if is_in_a_row(test_list) == answer:
			print("2: Pass")
		else:
			print("2: Fail")
	except:
		print("2: Fail")

def run_unittests():
	unittest1()
	unittest2()
	
if __name__ == "__main__":
	run_unittests()
		