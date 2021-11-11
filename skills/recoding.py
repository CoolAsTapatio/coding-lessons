# Untitled.py
# Created by Kids on 10/3/20.

who_records = {"luke bryan" : 400, "imagine dragons" : 500, "james taylor" : 300, "matisyahu" : 250, "one republic" : 300}
recording_hours = {"luke bryan" : 50, "carrie underwood" : 40, "matisyahu" : 50, "one republic" : 25, "billie eilish" : 2}
percentalbum = {"luke bryan" : 0.2, "kelly clarckson" : 0.15, "john legend" : 0.23, "089" : 0.50}
revenue = {"luke bryan" : 2000000, "matisyahu" : 150000, "lil nas x" : 2000000}
def get_percent(artist):
	if artist in percentalbum:
		return percentalbum[artist]
	else:
		answer = input("what percent does " + artist + " make?\n")
		return answer
		
def get_revenue(artist):
	if artist in revenue:
		return revenue[artist]
	else:
		answer = input("how much revenue does " + artist + " generate per album\n")
		return answer
def calc_studio_prof(artist):
	percent = float(get_percent(artist))
	revenue = float(get_revenue(artist))
	artist_profit = percent * revenue
	return revenue - artist_profit
	'''def artprof(the_artis):
	if the_artis in revenue:
		if the_artis in percentalbum:
			return revenue[the_artis] / percentalbum[the_artis]
		else:
			answer = input("what percent does " + the_artis + " make?\n")
			return revenue[the_artis] / answer
	else:
		answer = input("how much does " + the_artis + " make in revenue per album\n")
		return answer / percentalbum[the_artis]'''
		
def calc_total_cost_per_art(artist_name):
	time = get_hours(artist_name)
	rate = get_rate(artist_name)
	total_price = time * int(rate)
	return total_price 
	
def get_hours(who):
	if who in recording_hours:
		return recording_hours[who]
	else:
		artist_hours = input("how many hours does it take " + who + " to record an album\n")
		return artist_hours
		
def get_rate(artist):
	if artist in who_records:
		return who_records[artist]
	else:
		the_rate = input("what is the rate of " + artist + "  per hour in a recording studio\n")
		return the_rate
'''write a function that takes in an artist name and the amount of profit that we want to make as the studio and calculates how much revenue we need to make to have the album to generate the amount of profit that we want.'''
def BIGGGGG_func(artist, profit_hope):
	producing_expense = float(get_rate(artist)) * float(get_hours(artist))
	ownership_expenses = float(get_percent(artist))
	part_of_rev  = float(producing_expense + profit_hope)
	revenue = part_of_rev / (1 - ownership_expenses)
	return revenue
	#rev = (profit + p_exp) / (1 - rate)
	
	
		
if __name__ == "__main__":
	art = input("please give an artist\n")
	profit = int(input("how much profit are you hoping to make on this album?\n"))
	print(BIGGGGG_func(art, profit))