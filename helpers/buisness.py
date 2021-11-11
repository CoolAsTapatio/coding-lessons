# Untitled.py
# Created by Kids on 9/19/20.


def organizer(money_list):
	sum_ = 0
	for i in range(0, len(money_list), 1):
		sum_ = sum_ + money_list[i]
	return sum_ 
def profit_list_generator(revenuelist, expenselist):
	profit_list = []
	for s in range(0, len(revenuelist), 1):
		difference = revenuelist[s] - expenselist[s]
		profit_list.append(difference)
	return profit_list
def profit_org_2(revenue, expense):
	v = profit_list_generator(revenue, expense)
	the_sum = organizer(v)
	return_string = ""
	if the_sum > 0:
		return_string = "overall profit this quarter is " + str(the_sum)
	else:
		return_string = "overall loss this quarter is " + str(the_sum)
	return return_string
	
'''
	1) write a function that takes in a list of revenue and a list of expenses, calls the profit_list_generators function to get a list of profits, calls the organizer function on that list of profits, and then if the profit is negative, returns "Overall Loss this Quarter is $X." (where X is the sum of profit) and if the profit is positive, returns "Overall Profit this Quarter is $Y" (where Y is the sum of Profit).
	
	2) Call that new function from main passing in listofrevenue and expenses
'''


if __name__ == "__main__":
	listofrevenue = []	
	expenses = []	
	profit_creator = profit_list_generator(listofrevenue, expenses)
	total_profit = organizer(profit_creator)
	print("$" + str(total_profit))
	v = profit_org_2(listofrevenue, expenses)
	print(v)
	