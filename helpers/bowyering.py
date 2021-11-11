# Untitled 3.py
# Created by Kids on 1/23/21.
bow_type_ht = {'american recurve' : 600, 'english longbow' : 550, 'american flatbow' : 625, 'african' : 400, 'japanese' : 660, 'chinese' : 475, 'primitive' : 450, 'custom' : 700}
species_ht = {'ash': 60, 'hop hornbeam': 60, 'elm' : 80, 'maple' : 75, 'oak' : 75, 'hickory' : 90, 'osage' : 100, "pacific yew" : 110, 'port orford cedar' : 85, "eastern red cedar" : 85, "english yew" : 10 'custom' : 100, "black locust" : 100, "hazel" : 50}  
seasoning_ht = {'5' : 50, '6' : 60, '7': 75, '8' : 90, '9' : 110, '10' : 150}
is_it_white_wood_ht = [species_ht['ash'], species_ht['hop hornbeam'], species_ht['elm'], species_ht['maple'], species_ht['oak'], species_ht['hickory']]
backing_options_ht = {'none' : 0, 'snake skin' : 30, 'bison hide': 40, 'deer hide' : 40, 'clarified calfskin' : 40, 'sinew' : 50, 'custom' : 50}
string_material_ht = {'sinew' : 40, 'rawhide' : 30, 'hemp' : 20, 'flax': 30, 'premium flax' : 35, 'linen' : 30, "coconut fiber" : 35,'custom' : 40}
string_silencer_ht = {'none' : 0, 'fox' : 30, 'beaver' : 25, 'otter' : 25, "bobcat" : 30, 'custom' : 30}
handle_ht = {'none' : 0, 'leather' : 30, 'rawhide' : 20, 'deerhide' : 30, 'rabbit' : 20, 'custom' : 30}

class Bows:
	def __init__(self, backing, string_material, type_, hand, species, knots, seasoning, draw_weight, string_silencer):
		self.wood = Wood(species, knots, seasoning)
		self.string = String(string_material, string_silencer)
		self.bow_type = type_
		self.handle = hand
		self.backing = backing
		self.draw_weight = draw_weight
		self.price = 0
	def update_price(self):
		self.update_silencer_price()
		self.update_seasoning_price()
		self.update_handle_price()
		self.update_bow_type_price()
		self.update_speacies_price()
		self.update_string_material()
		self.update_knot_price()
		self.update_backing_price()
		self.set_weight_cost()
		return self.price
	def update_silencer_price(self):
		self.price += string_silencer_ht[self.string.silencer]
	def update_seasoning_price(self):
		self.price += seasoning_ht[self.wood.seasoning]
	def update_handle_price(self):
		self.price += handle_ht[self.handle]
	def update_bow_type_price(self):
		self.price += bow_type_ht[self.bow_type]
	def update_speacies_price(self):
		self.price += species_ht[self.wood.species]
	def update_string_material(self):
		self.price += string_material_ht[self.string.material]
	def update_knot_price(self):
		knots = self.wood.knots * 10
		knots = knots - (knots * 2)
		self.price += knots
	def update_backing_price(self ):
		self.price += backing_options_ht[self.backing]
	def set_weight_cost(self):
		if self.draw_weight == 45:
			self.price +=  0
		elif self.draw_weight < 45:
			new_var = 45 - self.draw_weight
			self.price += new_var * 10
		else:
			new_var = self.draw_weight - 45
			self.price += new_var * 10
class String:
	def __init__(self, material, silence):
		self.material = material
		self.silencer = silence		
class Wood:
	def __init__(self, species, knots, seasoning):
		self.species = species
		self.knots = knots
		self.seasoning = seasoning
if __name__ == '__main__':
	number_of_knots = int(input('how many knots would you think should be on your bow (one knot is that number multiplied by ten in a negative form (max of 8))?\n'))
	species___ = input('what species would you like your bow to be made of?\n')	
	string_mat = input('what would you like the bow string to be made of?\n')
	bow__type = input('what type of bow would you like?\n')
	hand = input('what type of handle would you like on your bow?\n')
	seasons = input('how many months would you like your bow stave to be seasoned for?\n')
	answer_weight = int(input('what would you like the draw weight of your bow to be?\n'))
	silence = input('what type of string silencer would you like?\n')
	if species___ in is_it_white_wood_ht:
		answer1 = input('your bow would be very well off with a backing, would you like one, yes or no?\n')
		if answer1 == 'yes':
			answer2 = input('what material would you like your bow to be backed with?\n')
		else:
			answer2 = "none"	
	else:
		answer1 = input("your bow doesn't need a backing do you want one?\n")
		if answer1 == "yes":
			answer2 = input('what material would you like your bow to be backed with?\n')
		else:
			answer2 = "none"
	the_bow = Bows(answer2, string_mat, bow__type, hand, species___, number_of_knots, seasons, answer_weight, silence) 
	print(the_bow.update_price())
