# Untitled.py
# Created by Kids on 9/29/20.

sports_team_stuff = {"christiano Ronaldo" : 109000000, "LeBron James" : 89000000, "Roger Federer" : 93000000, "James Harden" : 47000000, "Chris Paul" : 47000000}
def richer_athlete(Athlete1, Athlete2):
	ath1 = sports_team_stuff[Athlete1]
	ath2 = sports_team_stuff[Athlete2]	
	if ath1 < ath2:
		print(Athlete1 + " is less rich than " + Athlete2 + " who makes " + str(sports_team_stuff[Athlete2]))
	elif ath1 > ath2:
		print(Athlete2 + " is less rich than " + Athlete1 + " who makes " + str(sports_team_stuff[Athlete1]))
	else:
		print(Athlete1 + " is as rich as " + Athlete2 + " who makes " + str(sports_team_stuff[Athlete2]))
if __name__ == "__main__":
	richer_athlete("James Harden", "Chris Paul")