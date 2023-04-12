# Untitled.py
# Created by Kids on 7/26/22.
#Simple Program, Complex Program, App Development, Interface, Remodel of App, Remodel of Interface
def Price_Calc(Cooordinating_Hash, Request):
	Price = 0
	for i in Request:
		Price += Cooordinating_Hash[i]
	return Price
	
if __name__ == "__main__":
	Assignment_to_Price = {"Simple Program" : 300, "Complex Program": 500, "App Development" : 800, "Interface" : 750, "Remodel of App" : 400, "Remodel of Interface" : 300, "Web Development" : 450} #This Hash table maps each item of code to its price
	Tasks_Needed = ["Interface", "Interface", "Remodel of App", "Simple Program"]
	Price = Price_Calc(Assignment_to_Price, Tasks_Needed)
	print("The total cost of your requested programs will be $" + str(Price))
	exit()