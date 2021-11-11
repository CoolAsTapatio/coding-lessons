# Untitled.py
# Created by Kids on 9/29/20
revenue_year_ht = {1 : 100, 2 : 200, 3 : 300, 4 : 400, 5 : 500}
def revenueyear(year):
	return revenue_year_ht[year]

def revenue_lookup(year):
	if year not in revenue_year_ht:
		return "we have not projected that far into the future"
	else:
		return revenue_year_ht[year]
	
if __name__ == "__main__":
	var = int(input("please give me a number of one through five(years) for the projected revenue\n"))
	print(revenue_lookup(var))
'''
1) Write a function that takes in a number (representing the number of years), and looks up in a hashtable, the expected revenue (value) in that many years (key).
2) Ask the user for input on how many years they would like to look up the expected revenue for, and print out the expected revenue for them in main. 
'''