# Untitled.py
# Created by Kids on 9/26/20.
products_and_price = {"footstool/endtable" : 75, "bandsaw_style_box" : 75, "jewlerybox" : 30, "industraldesk" : 200, "future_product" :  100000}
cost_per_employee = {"brennan" : 0.05, "zoe" : 0.05, "theo" : 0.9}
	
def product_calc(product1, employee1):
	revenue = products_and_price[product1]
	expense_ratio = cost_per_employee[employee1]
	expense = revenue * expense_ratio
	profit = revenue - expense
	return profit

if __name__ == "__main__":
	print(product_calc("footstool/endtable", "brennan"))



'''
1) Make a function that takes in a product name (must be the exact same string as the keys in product and price HT) and employee name and returns the profit your business made (which is the money you got from the sale but didn't need to pay your employee. Make sure to use your hashtables you made above.
'''

