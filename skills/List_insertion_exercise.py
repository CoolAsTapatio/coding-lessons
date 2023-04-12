# Untitled 2.py
# Created by Kids
def list_inserter(lisT, element, index):
	first_chunk = lisT[0: index]
	last_chunk = lisT[index: ]
	first_chunk.append(element)
	for i in last_chunk:
		first_chunk.append(i)
	new_list = first_chunk
	return new_list
def main():
	pre_split_insertion_vars = input("what would you like to have inserted into a list (element, index): ")
	element, index = pre_split_insertion_vars.split(", ")
	my_list = ["hi", "high", "thigh", "thy", "thai", "tie", "why", "bye", "by", "nigh", "guy", "my", "shy", "sky", "buy", "pi", "pie", "cry", "lie", "sci", "psi", "psy", "eye"]
	print(list_inserter(my_list, element, int(index)))
	return
if __name__ == "__main__":
	main()