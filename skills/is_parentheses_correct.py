'''
c1: ()
c2: (())
c3: (()())
c4: (())()()
i1: )(
i2: ())
i3: )((()()()()()()(
i4; (
i5: )))))))))))))))))))))))))))))((((()()())())()))))))(()(

e1: )(
e2: ))((
e3: )
e4: ())

'''


def r_p_r(string, should_be_zero=0):
	if len(string) == 0:
		if should_be_zero == 0:
			return True
		else:
			return False
	else:
		if string[0] == "(":
			should_be_zero += 1
			new_string = string[1: ]
			return r_p_r(new_string, should_be_zero)
		elif string[0] == ")":
			if should_be_zero == 0:
				return False 
			else:
				should_be_zero -= 1
				new_string = string[1: ]
				return r_p_r(new_string, should_be_zero)
		else:
			new_string = string[1: ]
			return r_p_r(new_string, should_be_zero)
def unit_test_1():
	string_var = "()"
	expected_answer = True
	real_answer = r_p_r(string_var)
	assert(real_answer == expected_answer)
def unit_test_2():
	string_var = "())"
	expected_answer = True
	real_answer = r_p_r(string_var)
	assert(real_answer == expected_answer)
if __name__ == "__main__":
	unit_test_1()
	unit_test_2()