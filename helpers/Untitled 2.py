# Untitled 2.py
# Created by Kids on 1/12/21.

class Person:
	def __init__(self, myname, my_height, my_weight, my_dob, my_dod):
		self.name = myname
		self.height = my_height
		self.weight = my_weight
		self.dob = my_dob
		self.dod = my_dod
	def print_prop(self):
		print(self.name)
		print(self.height)
		print(self.weight)
		print(self.dob)
		print(self.dod)
if __name__ == "__main__":
	my_constructed_person = Person("Rubeus Hagrid", 10, 300, "1970", "unknown")
	new_object_ = Person("Ariana Dumbledore", 5.5, 100, "1920", "1940")
	new_object_.print_prop()