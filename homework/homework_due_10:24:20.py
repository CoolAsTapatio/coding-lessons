# Untitled.py
# Created by Kids on 10/24/20.


def is_it_here(a, b):
		for i in b:#O(l)
			for i2 in i: # O(l * e)
				if a == i2: # O(l * e)
					return "okay" 
		return "sorry"
if __name__  == "__main__":
	'''amswer = input("please give me a product that you would like to buy.\n")
	boxes = ["box 1", "box 2", "jewlery box"]
	bowls = ["salad bowl", "ramen bowl"]
	kitchen_ware = ["knife set", "cutting board", "coffee mugs"]
	Products = [kitchen_ware, boxes, bowls]'''
	
	print(is_it_here(amswer, Products))