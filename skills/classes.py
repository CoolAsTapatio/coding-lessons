# Untitled 4.py
# Created by Kids on 1/23/21.

class Author:
	def __init__(self, number_published, number_series, longest_series, name, gender, height, weight, dob, dod):
		self.num_pub = number_published
		self.num_ser = number_series
		self.length = longest_series
		self.name = name
		self.gender = gender
		self.height = height
		self.weight = weight		
		self.dob = dob
		self.dod = dod
	def printer(self):
		print(self.num_pub)
		print(self.num_ser)
		print(self.length)
		print(self.name)
		print(self.gender)
		print(self.height)
		print(self.weight)
		print(self.dob)
		print(self.dod)
def object_param_func(my_outhoor):
	my_outhoor.printer()
if __name__ == "__main__":
	j_k_rowling = Author(8, 2, 7, "J.K Rowling", "female", "?????", "????????", "?????", "future")
	object_param_func(j_k_rowling)