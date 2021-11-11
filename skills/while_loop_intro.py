import string
# Untitled.py
# Created by Kids on 8/28/20. 
i = 0
loop_done = False 
while not loop_done:
	#print("this following is true")
	i = i + 1
	if i > 10:
		loop_done = True
	
can_you_drink = False
how_old_are_you = 0
while not can_you_drink:
	if how_old_are_you == 20:
		whtiparent = input("are you with a parent?\n")
		if whtiparent.lower() == "yes":
			print("7777777 whiskeys comin right up.")	
	elif how_old_are_you == print("you need to be " +  str(21 - how_old_are_you) + " years older to get into the bar"):
		how_old_are_you = how_old_are_you + 1
	if how_old_are_you == 21:
		can_you_drink = True
		print("8888888 whiskeys comin right up.")
	how_old_are_you = how_old_are_you + 1