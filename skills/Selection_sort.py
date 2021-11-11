# Untitled 2.py
# Created by Kids on 9/16/21.
def selection_sorter(unsorted):
#	is_it_sorted_while_input = False
#	is_it_sorted = []
#	for t in unsorted:
#		is_it_sorted.append(False)
#		
#	for i in range(0, len(unsorted)):
#		if i == 0:
#			is_it_sorted[i] = True
#		else:
#			if unsorted[i] >= unsorted[i-1]:
#				is_it_sorted[i] = True
#		
#	truth = len(is_it_sorted)
#	for i in is_it_sorted:
#		if i == True:
#			truth =- 1
#			
#	if truth == 0:
#		return "yaaas"
#		is_it_sorted_while_input = True
#	else:
#		return "nooooooooo"
	
	for i in range(0, len(unsorted)):
		the_min = min(unsorted[i: ])
		index_of_current_min = 0
		for t in range(i, len(unsorted)):
			if unsorted[t] == the_min:
				index_of_current_min = t
		unsorted = swap(unsorted, i, index_of_current_min)
		#print(unsorted)
	return unsorted	
	
def swap(unsorted, in1, in2):
	element2 = unsorted[in2]
	unsorted[in2] = unsorted[in1]
	unsorted[in1] = element2
	return unsorted


def swap_unit_test_1():
	list_ = [3, 6, -1, 3, 5, 2]
	expected = [-1, 6, 3, 3, 5, 2]
	result = swap(list_, 0, 2)
	assert(result == expected)
	
def selection_sorter_unit_test_1():
	list_ = [3, 6, -1, 3, 5, 2]
	expected = [-1, 2, 3, 3, 5, 6]
	result = selection_sorter(list_)
	assert(result == expected)
	
def selection_sorter_unit_test_2():
	list_ = [32, 6.3, -1, 3.55, 5, 2]
	expected = [-1, 2, 3.55, 5, 6.3, 32]
	result = selection_sorter(list_)
	assert(result == expected)
	
def run_unit_tests():
	selection_sorter_unit_test_1()
	selection_sorter_unit_test_2()
if __name__ == "__main__":
	run_unit_tests()
	list_creator_input = input("please put in a list of numbers to be sorted (separted by  )\n")
	list_string_splitter = list_creator_input.split(", ")
	unsorted = []
	for i in list_string_splitter:
		i = int(i)
		unsorted.append(i)
	print(selection_sorter(unsorted))
#	for t in unsorted:
#		print(t)
#		print(type(t))