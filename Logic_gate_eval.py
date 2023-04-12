# Untitled.py
# Created by Kids on 4/27/22.
#
# valid: AND(True, NOT(False))
# valid: NOT(NOR(XOR (   True, False) ,    NOT(True)))
# valid: NAND(True,XOR(False, True))
# invalid: not(True)
# invalid: NR(AND(True, False), False)
# invalid: NOT(false)
# AND(False
#
def main(request):
	
	if request == "done":
		exit()
	else:
		request = request.replace(" ", "")
#		for i in range(0, len(request)):
#			if request[i] == " ":
#				request = request[0: i] + request[i+1: ]
		first_comma = request.index(",")
		gate_and_first_bool, second_bool = request[0: first_comma], request:[first_comma + 1 :]
		if gate_and_first_bool[-2] = "s" and ")" not in gate_and_first_bool:
			gate = gate_and_first_bool[0: -6]
			first_bool = False
		elif ")" not in gate_and_first_bool:
			gate = gate_and_first_bool[0: -5]
			first_bool = False
		else:
			first_bool = main(gate_and_first_bool)
			
			#working here
		if gate == "AND":
			return and_()
		elif gate == "NAND":
			return not_(and_())
		elif gate == "NOT":
			return not_()
		elif gate == "OR":
			return or_()
		elif gate == "NOR":
			return not_(or_())
		elif gate == "XOR":
			return xor_()
		print(request)
		exit()
	
def xor_(first_bool, second_bool):
	if first_bool, second_bool == True, False or first_bool, second_bool = False, True:
		return True
	else:
		return False
		
def or_(first_bool, second_bool):
	if first_bool, second_bool == False, False:
		return False
	else:
		return True

def not_(bool_):
	if bool_ == True:
		return False
	else:
		return True	
				
def and_(first_bool, second_bool):
	if first_bool == second_bool:
		return True
	else:
		return False
		

if __name__ == "__main__":
	request = input("what truth expression would you like to have evaluated: ")
	main(request)
