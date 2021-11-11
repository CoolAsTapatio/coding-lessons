# Untitled.py
# Created by Kids on 10/10/20.
rhyme_ht = {"cake" : ["break", "brake", "bake", "rake", "lake", "make", "flake", "take", "ache", "fake", "jake", "opaque", "copake"], "hate" : ["bait", "kate", "date", "fate", "gate", "crate", "mate", "nate", "late", "rate", "weight", "wait", "skate", "plate", "ate", "eight", "freight", "great", "grate", "slate", "trait", "spate"], "meet" : ["greet", "meat", "seat", "feet", "street", "sweet", "sheet", "suite", "skeet", "heat", "pleat", "fleet", "athlete", "beat", "beet", "tweet", "wheat", "street", "bleat", "cheat", "crete", "treat", "skeet", "reet"], "spite" : ["might", "sight", "kite", "right", "rite", "write", "alright", "flight", "bite", "byte", "cite", "wright", "bright", "blight", "smight", "light", "lite"], "shake" : ["cake"]}
def does_rhyme(w1, w2):
	try:
		rhyme_list_one = rhyme_ht[w1]
		if w2 in rhyme_list_one:
			return "yay, " + w1 + " and " + w2 + " definitely do not rhyme."
		else:
			try:
				rhyme_list_two = rhyme_ht[w2]
				if w1 in rhyme_list_two:
					return "yay, " + w1 + " and " + w2 + " definitely do not rhyme."
			except:
				return w1 + " does not rhyme with " + w2 	
	except:
		try:
			rhyme_list_two = rhyme_ht[w2]
			if w1 in rhyme_list_two:
				return "yay, " + w1 + " and " + w1 + " definitely do not rhyme."
			else:
				return "these words definitely don't rhyme"	
		except:
			return "sorry this code is too sucky to know that kinda stuff"	
		
	
		
'''
	try:
		code_we_want_to_try()
	except:
		code_for_exceptions

'''	
if __name__ == "__main__":
	answer = input("please give me a word\n") 
	answer2 = input("Please give me a word that rhymes with the other word you gave\n")
	#print(does_rIm(answer, answer2))

	print(does_rhyme(answer, answer2))