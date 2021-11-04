import random

saved_boolean = [False, False, False, False, False]
commands = ["exit", "roll", "save", "unsave", "score", "show score", "reset"]
valid_scores = ["yahtzee", "full house", "large straight", "small straight", "four of a kind", "three of a kind", "chance", "1", "2", "3", "4", "5", "6"]
scoreht = {"yahtzee" : None, "full house" : None, "large straight" : None, "small straight" : None, "four of a kind" : None, "three of a kind" : None, "chance" : None, "1" : None, "2" : None, "3" : None, "4" : None, "5" : None, "6" : None, "yahtzee_bonus" : 0, "upper_bonus" : 0} 
scores_left = 13
upper_score_total = 0
game_total_score = 0
dice = [None, None, None, None, None]
def driver():
	global game_total_score
	global scores_left
	global upper_score_total
	game_running = True
	rolls_taken = 0
	while game_running:
		if scores_left == 0:
			#if game_total_score == 
			print("good game. your score was " + str(game_total_score) + ".")
			play_again = input("do you want to play again (Y/N): ")
			if play_again == "Y":
				reset()
			else:
				exit()
		what_player_wants = input("what would you like to do next?: ")
		if what_player_wants not in commands:
			print("that is not a proper command\n")
		else:
			if what_player_wants == "reset":
				reset()
			if what_player_wants == "unsave":
				unsave()
			elif what_player_wants == "exit":
				print("ok, good game.")
				game_running = False
			elif what_player_wants == "roll":
				if rolls_taken < 3:
					roll()
					rolls_taken += 1
				elif rolls_taken == 3:
					print("this is cheating")
					rolls_taken += 1
				else:
					print("bruh")
					rolls_taken += 1
			elif what_player_wants == "save":
				if rolls_taken > 0:
					save()
				else:
					print("this is cheating")
			elif what_player_wants == "score":
				if rolls_taken > 0:
					if score() == True:
						rolls_taken = 0
				else:
					print("please roll first")
			elif what_player_wants == "show score":
				print("\nupper score total is " + str(upper_score_total))
				print("the total score is " + str(game_total_score))
				print(scoreht)
def reset():
	global scores_left
	global game_total_score
	global upper_score_total
	reset_saves()
	for i in scoreht:
		if i != "yahtzee_bonus" and i != "upper_bonus":			
			scoreht[i] = None
		else:
			scoreht[i] = 0
	for v in dice:
		v = None
	scores_left = 13
	upper_score_total = 0
	game_total_score = 0
		
def score():
	global scores_left
	global game_total_score
	global upper_score_total
	choice = input("what scoring option would you like to do?: ")
	if choice in scoreht:
		if scoreht[choice] is None:
			this_score = calc_score(choice)
			if this_score == 0:
				zero_input = input("your score is zero, would you like to take that? (Y/N): ")
				if zero_input == "Y":
					scoreht[choice] = 0
					reset_saves()
					print(scoreht)
					scores_left -= 1	
					return True
				else:
					return False
			else:
				reset_saves()
				if choice == "yahtzee bonus" and this_score == 100:
					scoreht["yahtzee bonus"] += 100
				elif choice != "yahtzee bonus":
					scoreht[choice] = this_score
					scores_left -= 1
				if choice == "1" or choice == "2" or choice == "3" or choice == "4" or choice == "5" or choice == "6":
					upper_score_total += scoreht[choice]
					calc_upper_bonus()
				game_total_score += scoreht[choice]
				print(scoreht)
				return True
		else:
			print("you've already taken " + choice + ", choose a different one\n")
			return False
	else:
		print(choice + " is not a valid scoring option")
		return False
def reset_saves():
	for i in range(0, len(saved_boolean)):
		saved_boolean[i] = False
def calc_score(the_choice):
	if the_choice == "cancel":
		return False
	if the_choice == "yahtzee bonus":
		return yahtzee_bonus_scorer()
	if the_choice == "yahtzee":
		return yahtzee_scorer()
	if the_choice == "large straight":
		return large_straight_scorer()
	if the_choice == "small straight":
		return small_straight_scorer()
	if the_choice == "1":
		return ones_score()	
	if the_choice == "2":
		return twos_score()
	if the_choice == "3":
		return threes_score()	
	if the_choice == "4":
		return fours_score()
	if the_choice == "5":
		return fives_score()
	if the_choice == "6":
		return sixes_score()
	if the_choice == "four of a kind":
		return four_of_a_kind_scorer()
	if the_choice == "three of a kind":
		return three_of_a_kind_scorer()
	if the_choice == "chance":
		return chance_scorer()
	if the_choice == "full house":
		return full_house_scorer()
def yahtzee_bonus_scorer():
	if scoreht["yahtzee"] == 50:
		if dice[1] == dice[2] and dice[1] == dice[3] and dice[1] == dice[4] and dice[1] == dice[5]:
			 return 100
def calc_upper_bonus():
	global game_total_score
	global upper_score_total
	if scoreht["upper_bonus"] == 0:
		if upper_score_total >= 63:
			scoreht["upper_bonus"] = 35
			upper_score_total += 35
			game_total_score += 35
def full_house_scorer():
	sorted_dice = sorted(dice)
	if (sorted_dice[0] == sorted_dice[1] and sorted_dice[2] == sorted_dice[3] and sorted_dice[3] == sorted_dice[4]) or (sorted_dice[0] == sorted_dice[1] and sorted_dice[1] == sorted_dice[2] and sorted_dice[3] == sorted_dice[4]):
		return 25
	else:
		return 0
def chance_scorer():
	return sum(dice)
def three_of_a_kind_scorer():
	sorted_dice = sorted(dice)
	if (sorted_dice[0] == sorted_dice[1] and sorted_dice[1] == sorted_dice[2]) or (sorted_dice[1] == sorted_dice[2] and sorted_dice[2] == sorted_dice[3]) or (sorted_dice[2] == sorted_dice[3] and sorted_dice[3] == sorted_dice[4]):
		return sum(sorted_dice)
	else:
		return 0
def sixes_score():
	NUMBER = 6
	_score = 0
	for i in dice:
		if i == NUMBER:
			_score += NUMBER
	return _score
def fives_score():
	NUMBER = 5
	_score =0
	for i in dice:
		if i == NUMBER:
			_score += NUMBER
	return _score		
	#return 0
def four_of_a_kind_scorer():
	sorted_dice = sorted(dice)
	if (sorted_dice[0] == sorted_dice[1] and sorted_dice[1] == sorted_dice[2] and sorted_dice[2] == sorted_dice[3]) or (sorted_dice[1] == sorted_dice[2] and sorted_dice[2] == sorted_dice[3] and sorted_dice[3] == sorted_dice[4]):
		return sum(sorted_dice)
	else:
		return 0	
def ones_score():
	NUMBER = 1
	_score = 0
	for i in dice:
		if i == NUMBER:
			_score += NUMBER
	return _score
def twos_score():
	NUMBER = 2
	_score = 0
	for i in dice:
		if i == NUMBER:
			_score += NUMBER
	return _score
def threes_score():
	NUMBER = 3
	_score = 0
	for i in dice:
		if i == NUMBER:
			_score += NUMBER
	return _score
def fours_score():
	NUMBER = 4
	_score = 0
	for i in dice:
		if i == NUMBER:
			_score += NUMBER
	return _score	
'''
def sss_un1():
	test_dice = [2, 6, 5, 5, 3]
	assert(small_straight_scorer(test_dice) == 0)
def sss_un2():
	test_dice = [1, 2, 4, 6, 3]
	assert(small_straight_scorer(test_dice) == 30)
def sss_un3():
	test_dice = [1, 2, 3, 4, 3]
	assert(small_straight_scorer(test_dice) == 30)
def sss_un4():
	test_dice = [6, 4, 3, 2, 1]
	assert(small_straight_scorer(test_dice) == 30)
	'''
def small_straight_scorer():
	sorted_dice = sorted(dice)
	if (sorted_dice[0] + 1 in sorted_dice and sorted_dice[0] + 2 in sorted_dice and sorted_dice[0] + 3 in sorted_dice) or (sorted_dice[1] + 1 in sorted_dice and sorted_dice[1] + 2 in sorted_dice and sorted_dice[1] + 3 in sorted_dice):
		return 30
	else:
		return 0
def large_straight_scorer():
	sorted_dice = sorted(dice)
	if sorted_dice[0] + 1 == sorted_dice[1] and sorted_dice[1] + 1 == sorted_dice[2] and sorted_dice[2] + 1 == sorted_dice[3] and sorted_dice[3] + 1 == sorted_dice[4]:
		return 40
	else:
		return 0
def yahtzee_scorer():
	if dice[0] == dice[1] and dice[0] == dice[2] and dice[0] == dice[3] and dice[0] == dice[4]:
		return 50
	else:
		return 0
'''def valid_unsave(to_unsave):
	while val
	if len(to_unsave > 5:
		return -1
	'''
def save():
	global saved_boolean
	global dice
	# 1) making sure with 33211 we can actually save both 3s, 2) making sure to handle scenario where user wants to save 6 but you rolled all 4s, 3) handling incorrect input
	try:
		saved_input = input("what values of dice (separated by a comma and space) would you like to save (NUMBERs ONLY pls): ")
		
		saved_input_list = saved_input.split(", ")
		int_saved_input_list = [int(i) for i in saved_input_list]
		for s in range(0, len(int_saved_input_list)):
			this_num = int_saved_input_list[s]	
			# input of 1 1 3 3, on first iteration of s, s=0, this_num = 1, int_saved_input_list = 1 3 3	
			for i in range(0, len(dice)):
				if dice[i] == this_num and saved_boolean[i] == False:
					saved_boolean[i] = True
					break		
	except:
		print("enter numbers separated by commas")
def unsave():
	global saved_boolean
	global dice
	try:
		unsaved_input = input("what values of dice (separated by a comma and space), 1 through 6, would you like to unsave?: ")
		unsaved_input_list = unsaved_input.split(", ")
		print(unsaved_input_list)
		for i in unsaved_input_list:
			unsave_val = int(i)
			for s in range(0, len(dice)):
				if unsave_val == dice[s] and saved_boolean[s] == True:
					saved_boolean[s] = False
					break
#				#else
	except:
		print("enter numbers separated by commas")
def roll():
	for i in range(0, len(dice)):
		if saved_boolean[i] == False:
			dice[i] = random.randint(1, 6)
	print("your dice are ", dice)
if __name__ == "__main__":
	driver()