# Untitled.py
# Created by Kids on 1/17/23.
def strip_spaces(starter):
	return starter.replace(" ", "")
def remove_spaces(starter):
	return "".join(starter.split())
def remove_leading_whitespace(starter):
	return starter.lstrip()
def remove_trailing_whitespace(starter):
	return starter.rstrip() + "|"
def remove_whitespace(starter):
	return starter.strip()
def replace_characters(starter, to_replace, to_replace_with):
	return starter.replace(to_replace, to_replace_with)
	
	
	
	
	
	
	
def replace_nth_instance(starter, to_replace, to_replace_with, n):
	tracker = []
	for i in range(0, len(starter)): #iterates though OG string
		for i2 in range(0, len(to_replace)): #iterates through substring you want to replace
			print("starter " + starter[i+i2])
			print("\n starter " + to_replace[i2] + "\n")
			if starter[i+i2] != to_replace[i2]:
				print("breaking")
				break
			if i == len(to_replace):
				
				tracker += i
	print(tracker)
	starter[tracker[1] - starter[tracker[1]] + len(to_replace)] = to_replace_with
					
		#use nested loop to check substring and slice







def unit_test_rni():
	to_pass_in = "Zoe turned in Zoe's homework to Zoe's school for her"
	expected = "Zoe turned in Theo's homework to Zoe's school for her"
	result = replace_nth_instance(to_pass_in, "Zoe", "Theo", 2)
	assert(to_pass_in == expected)

if __name__ == "__main__":
#	unit_test_rni()
#	print(strip_spaces("hi how are you?"))
#	print("\n")
#	print(remove_spaces("hi how are you?"))
#	print("\n")
#	print(remove_leading_whitespace("        hi how are you?"))
#	print("\n")
#	print(remove_trailing_whitespace("hi how are you?      "))
#	print("\n")
#	print(remove_whitespace("          hi how are you?      "))
#	print("\n")
#	print(replace_characters("Theo thinks through thought-provoking theoretical code.", "t", "T"))
#	print("\n")
	print(replace_nth_instance("Zoe completed Zoe's homework by the deadline Zoe's teacher gave.", "Zoe", "Theo", 2))