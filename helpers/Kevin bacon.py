# Untitled.py
# Created by Kids on 2/23/2
'''theo = ["steve", "pam", "zoe", "janis", "andy", "donna", "linn", "joe", "noa", "george", "amiyah", "rayn", "dylan", "luca", "pete"]
steve = ["theo", "pam", "zoe", "janis", "andy", "donna", "linn" "joe", "jason", "mike", "todd", "steve", "david", "melissa", "jill"]
pam = [steve, pam, zoe, janis, andy, donna, linn, joe,]
zoe = [steve, pam, zoe, janis, andy, donna, linn, joe,]
janis = [steve, pam, zoe, janis, andy, donna, linn, joe,]
andy = [steve, pam, zoe, janis, andy, donna, linn, joe,]
donna = [steve, pam, zoe, janis, andy, donna, linn, joe,]
linn = [steve, pam, zoe, janis, andy, donna, linn, joe,]
joe = [steve, pam, zoe, janis, andy, donna, linn, joe,]'''
steve_knows = ["george stephenopoulos", "peter jennings", "allen keys", "jason morris", "hilary clinton", "mike lupica", "john mccain", "chris collins", "michael jordan", "zadie", "zadie", "donna", "staci", "theo", "zoe", "pam", "jerry", "david", "vanessa", "melissa"]
papa_joe_knows = ["steve", "andy", "linn", "janis", "christopher", "roberta", "theo", "zoe", "christopher", "tommy", "pam"]
theo_knows = ["papa joe", "steve", "tutu", "pam", "zadie", "jason", "jenny", "dylan", "amiyah", "george", "rayn", "luca", "pablo", "noa", "annabelle", "sean"]
zoe_knows = ["quinn", "isa", "savi", "jack", "xylem", "challotte", "aidan", "natalie", "maddie", "dylan", "clark", "vivian", "tyler", "kyler", "mason"]
pam_knows = ["kendra", "susanna", "lauren", "micky", "andy", "andrea", "andrea farber", "dan unger", "tommy", "dana", "malia"]
jmo_knows = ["judy woodruff", "jeremy steiner", "steph mo", "kmo", "donna", "mike", ""]
george_knows = ["joe biden", "barack obama", "michelle obama", "kamala harris", "luke bryan", "katy perry", "ryan seacrest", "lionel richie"]
katy_knows = ["glen bernard", "christena aguilera", "alanis morissette", "kelly clarkson"]
kelly_knows = ["john legend", "gwen stefani", "blake shelton", "nick jonas", "jason aldean"]
ht_peeps = {"papa joe" : papa_joe_knows, "steve" : steve_knows, "theo" : theo_knows, "zoe" : zoe_knows, "pam" : pam_knows, "jason morris" : jmo_knows, "george stephenapoulos" : george_knows, "katy perrry" : katy_knows, "kelly clarkson" : kelly_knows}
def bacon_degrees(person1, person2, visited=[], counted=1, min_=1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901):
	print(person1 + " + " + str(ht_peeps[person1]))
	if person2 in ht_peeps[person1]:
		return counted
	for i in ht_peeps[person1]:
		if person2 == i:
			return counted
		else:
			if i in ht_peeps and i not in visited:
				a = bacon_degrees(i, person2, visited+[person1], counted+1)
				if a is not None:
					if a < min_:
						min_ = a
	return min_					
if __name__ == "__main__":
	answer_p1 = input("who would you like one of the persons to be connected to to be?\n")
	answer_p2 = input("who would you the other of the persons to be connected to to be?\n")
	print(bacon_degrees(answer_p1, answer_p2))
	