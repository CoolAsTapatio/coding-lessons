import random
until_you_die = 0
list_of_words_to_play_with = ["wand", "incantation", "charm", "hallow", "horcrux", "ministry", "patron", "beater", "seeker", "chaser", "keeper", "proffesor", "forbidden"]
def single_player_driver(to_be_guessed, current_state):
	global until_you_die
	until_you_die = 0
	while "_" in current_state:
		if until_you_die == 6:
			are_they_playing_again = input("you died, will you return as a ghost to haunt the thing that killed you (play again (Y/N))?\n")
			if are_they_playing_again == "Y":
				driver()
			else:
				exit()
		else:
			what_would_you_like_to_do = input("what would you like to do?\n")
			if what_would_you_like_to_do == "guess":
				new_current_state = guess(current_state, to_be_guessed)
				current_state = new_current_state
				print(new_current_state)
			elif what_would_you_like_to_do == "quit":
				print("sore loser")
				exit()
	are_they_playing_again_win = input("you win, would you like to play again (Y/N)?\n")
	if are_they_playing_again_win == "Y":
		driver()
	else:
		exit
def guess(current_state, to_be_guessed):
	global until_you_die
	guessed_letter = input("what letter are you guessing right now?\n")
	if guessed_letter in to_be_guessed:
		for i in range(0, len(to_be_guessed)):
			if to_be_guessed[i] == guessed_letter:
				current_state = current_state[0 : i*2 + 1] + guessed_letter + current_state[i*2 + 2 : ] 
	else:
		until_you_die += 1
		print_hangman()
	return current_state
def print_hangman():
	global until_you_die
	if until_you_die == 1:
		print(" O")
	elif until_you_die == 2:
		print(" O")
		print(" |")
	elif until_you_die == 3:
		print(" O")
		print(" |-")
	elif until_you_die == 4:
		print(" O")
		print("-|-")
	elif until_you_die == 5:
		print(" O")
		print("-|-")
		print("/")
	elif until_you_die == 6:
		print(" O")
		print("-|-")
		print("/ \\")
def driver():
	global until_you_die
	until_you_die = 0
	what_version_would_you_like = input("would you like to play single player or multiplayer hangman?\n")
	if what_version_would_you_like == "single":
		single_player()
	elif what_version_would_you_like == "multiplayer":
		multiplayer()
def multiplayer():
	current_state = ""
	secret_word = input("what word would you like the other player to guess?\n")
	print(' \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
	for i in range(0, len(secret_word)):
		current_state += " _"
	print(current_state)
	single_player_driver(secret_word, current_state)
def single_player():
	global list_of_words_to_play_with
	to_be_guessed_index = random.randint(0, len(list_of_words_to_play_with)-1)
	to_be_guessed = list_of_words_to_play_with[to_be_guessed_index]
	current_state = ""
	for i in range(0, len(to_be_guessed)):
		current_state += " _"
	print(current_state)
	single_player_driver(to_be_guessed, current_state)
if __name__ == "__main__":
	driver()
	
'''
when guessed_letter is guessed, have an empty list that fills itselft with guessed_letter and check if it is already in list, if so print(you have already guess this, please guess something else), if not, proceed as normal exit
'''