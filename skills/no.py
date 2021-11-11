# Untitled.py
# Created by Kids on 12/12/20.


# {()} - valid
#  (([]))
#  ([)]
#. []
[(])
)(

def parent_braket(string, should_be_zero_parent=0, should_be_zero_braket=0):
	if len(string) == 0:
		if should_be_zero_parent == 0 and should_be_zero_braket == 0:
			return True
		else:
			return False	
	else:
		if string[0] == "(":
			new_string = string[1: ]
			should_be_zero_parent = should_be_zero_parent + 1
			return parent_braket(new_string, should_be_zero_parent, should_be_zero_braket)
		elif string[0] == ")":
			new_string = string[1: ]
			should_be_zero_parent = should_be_zero_parent - 1
			return parent_braket(new_string, should_be_zero_parent, should_be_zero_braket)
		elif string[0] == "[":
			new_string = string[1: ]
			should_be_zero_parent = should_be_zero_braket + 1
			return parent_braket(new_string, should_be_zero_parent, should_be_zero_braket)
		else:
			new_string = string[1: ]
			should_be_zero_parent = should_be_zero_braket - 1
			return parent_braket(new_string, should_be_zero_parent, should_be_zero_braket)
if __name__ == "__main__":
	print(parent_braket("([])", ))