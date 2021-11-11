# Untitled.py
# Created by Kids on 10/10/20.

names_ranked = {"zoe" : "meh", "pam" : "okay", "steve" : "fine", "theo" : "da best"}
def rank_returner(name):
	if name in names_ranked:
		return name +  " is " + names_ranked[name]
	else:
		return "wrong!!!!!!!"
def rank_returner_try(name):
	try:
		return names_ranked[name]
	except KeyError:
		return "wrong!!!!!!!!!!!!!!!!!"
def rank_retrun(name):
	return names_ranked[name]		
if __name__ == "__main__":
	answer = input("please give me a name\n")
	print(rank_returner_try(answer))