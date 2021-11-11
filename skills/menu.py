topping_options = input("what are the topping options(separated by a comma and a space)?\n")
topping_options_list = topping_options.split(", ")
serving_ht = {}
def driver():
	still_serving = True
	while still_serving == True:
		person_viewed = input("what person's order do you need to see?\n")
		print(person_viewed + " wants " + serving_ht[person_viewed])
		are_you_done = input("are you still serving?(Y/N)\n")
		if are_you_done == "Y":
			still_serving = False
def	per_person():
	global topping_options
	global serving_ht
	orders_taken = True
	while orders_taken == True:
		name__ = input("what is your name?\n")
		print("The topping options are " + topping_options)
		toppings = input("what toppings would you like?\n")
		serving_ht[name__] = toppings
		_are_you_done_taking_orders = input("are you done taking orders(Y/N)?\n")
		if are_you_done == "Y":
			orders_taken = False
if __name__ == "__main__":
	per_person()
	driver()