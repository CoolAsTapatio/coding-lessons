# Untitled.py
# Created by Kids on 2/16/21.
drinksht = {"old fashioned" : 30, "margherita" : 25, "straight up": 20, "on the rocks" : 25}
class Drinks:
	def __init__(self, carbonation, thickness, name, brand, flavor):
		self.carbon = carbonation
		self.thick = thickness
		self.name = name
		self.brand = brand
		self.flavor = flavor
	def get_thick(self):
		return self.thick
	def get_carbon(self):
		return self.carbon
	def get_name(self):
		return self.name
	def get_brand(self):
		return self.brand
	def get_flavor(self):
		return self.flavor
	def set_thick(self, val):
		self.thick = val
	def set_name(self, val):
		self.brand = val
	def set_brand(self, val):
		self.brand = val
	def set_flavor(self, val):
		self.flavor = val
class Alcohol(Drinks):
	def __init__(self, carb, thick, name, brand, fla, proof):
		self.proof = proof
		self.price = 0
		Drinks.__init__(self, carb, thick, name, brand, fla)
	def update_drink_price(self):
		self.price += drinksht[self.get_name()]
	def updatproofprice(self):
		self.price += self.proof / 2 + 5
	def update_carb_price(self):
		if self.carbon == True:
			self.price += 10
		else:
			self.price += 0		
	def update_price(self):
		self.update_carb_price()
		self.updatproofprice()
		self.update_drink_price()
		return self.price	
if __name__ == "__main__":
	answer_carb = bool(input("is your drink carbonated?\n"))
	print(answer_carb)
	answer_thick = int(input("how thick is your drink\n"))
	answer_drink = input("what type of drink are you having?\n")
	answer_brand = input("what brand of achohol is this\n")
	answer_flav = input("what flavor is your drink\n")
	answer_proof = int(input("what is the proof of your drink\n"))
	my_method_to_get_drunk = Alcohol(answer_carb, answer_thick, answer_drink, answer_brand, answer_flav, answer_proof)
	print(my_method_to_get_drunk.update_price())