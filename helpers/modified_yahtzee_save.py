## Untitled 2.py
## Created by Kids on 4/10/21.
import random
#
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
#def valid_save(to_save):
#	if len(to_save) > 5:
#		return False
#	else:
#		for i in to_save:
#			if i < 0 or i > 4:
#				return False
#		return True
#'''
#def valid_unsave(to_unsave):
#	while val
#	if len(to_unsave > 5:
#		return -1
#'''
#
#def valid_unsave(to_unsave):
#	if len(to_unsave) > 5:
#		return False
#	else:
#		for i in to_unsave:
#			if i < 0 or i > 4:
#				return False
#		return True
#
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
#
#	try:
#		unsaved = input("what number/s (separated by a comma and space) dice 1 through dice 5, would you like to unsave?: ")
#		unsaved_list = unsaved.split(", ")
#		unsaved_index_list = [int(i) - 1 for i in unsaved_list]
#		if valid_unsave(unsaved_index_list):
#			for i in unsaved_index_list:
#				saved_boolean[i] = False
#		else:
#			print("sorry, no changes have been made, those aren't valid dice to unsave, you can try typing in 'unsave' again and entering valid dice")
#	except:
#		print("enter numbers separated by commas")

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

def roll():
	for i in range(0, len(dice)):
		if saved_boolean[i] == False:
			dice[i] = random.randint(1, 6)
	print("your dice are ", dice)

if __name__ == "__main__":
	driver()	