# Untitled.py
# Created by Kids on 10/19/20.
product_list = ["box 1", "chair", "table", "box 2", "box 3", "urn", "mug", "bowl", "pen"]
def do_we_have_it(answer):
	if answer in product_list:  #O(n)
		return "great! we have this in stock, comin' right up!" # O(1) for either of these, only one will happen
	else:
		return "sorry, we do not have this product at the moment."	
if __name__ == "__main__":
	answer = input("please give a product that you would like to buy\n") # O(1)
	print(do_we_have_it(answer)) #O(1) total O(9)
		