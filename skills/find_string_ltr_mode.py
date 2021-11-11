# Untitled.py
# Created by Kids on 8/24/21.

'''def most_pop_ltr(string):
	lets = []
	for i in range(len(string)):
		if i in lets:
			lets[i] += 1
	max_let = max(lets)
	return max_let'''
def most_pop_ltr(wd):
	if len(wd) == 0:
		return "There are no letters."
	ht_of_indv_ltrs = {}
	for i in wd:
		if i in ht_of_indv_ltrs:
			ht_of_indv_ltrs[i] += 1
		elif i not in ht_of_indv_ltrs:
			ht_of_indv_ltrs[i] = 1
	mode_int = 1
	for f in ht_of_indv_ltrs:
		if ht_of_indv_ltrs[f] > mode_int:
			mode_int = ht_of_indv_ltrs[f]
	list_of_modes = []
	for t in ht_of_indv_ltrs:
		if ht_of_indv_ltrs[t] == mode_int:
			list_of_modes.append(t)
	final_list_of_letters = sorted(list_of_modes)
	finished_string = ""
	for s in final_list_of_letters:
		finished_string += s
		finished_string += " and "
	finished_string = finished_string[: -5]
	return finished_string
def unittest1():
	try:
		test_input = "hello"
		expected = "l"
		result = most_pop_ltr(test_input)
		print(result)
		if result == expected:
			print("Test 1: PASS")
		else:
			print("else")
			print("Test 1: FAIL")
	except:
		print("exept")
		print("Test 1: FAIL")

def unittest2():
	try:
		test_input = "splits"
		expected = "s"
		result = most_pop_ltr(test_input)
		if result == expected:
			print("Test 2: PASS")
		else:
			print("Test 2: FAIL")
	except:
		print("Test 2: FAIL")

def unittest3():
	try:
		test_input = "akkkallp"
		expected = "k"
		result = most_pop_ltr(test_input)
		if result == expected:
			print("Test 3: PASS")
		else:
			print("Test 3: FAIL")
	except:
		print("Test 3: FAIL")
		
def unittest4():
	try:
		test_input = "mmanny"
		expected = "m and n"
		result = most_pop_ltr(test_input)
		if result == expected:
			print("Test 4: PASS")
		else:
			print("Test 4: FAIL")
	except:
		print("Test 4: FAIL")
		
def unittest5():
	try:
		test_input = "late"
		expected = "a and e and l and t"
		result = most_pop_ltr(test_input)
		if result == expected:
			print("Test 5: PASS")
		else:
			print("Test 5: FAIL")
	except:
		print("Test 5: FAIL")
		
def unittest6():
	try:
		test_input = "climb"
		expected = "b and c and i and l and m"
		result = most_pop_ltr(test_input)
		if result == expected:
			print("Test 6: PASS")
		else:
			print("Test 6: FAIL")
	except:
		print("Test 6: FAIL")
		
def unittest7():
	try:
		test_input = ""
		expected = "There are no letters."
		result = most_pop_ltr(test_input)
		if result == expected:
			print("Test 7: PASS")
		else:
			print("Test 7: FAIL")
	except:
		print("Test 7: FAIL")
		
def main():
	unittest1()
	unittest2()
	unittest3()
	unittest4()
	unittest5()
	unittest6()
	unittest7()
	
if __name__ == "__main__":
	main()