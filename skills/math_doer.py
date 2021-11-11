# Untitled.py
# Created by Kids on 10/13/20.
def math_doer(a, b):	
	try:
		t1 = a/ b
	except ZeroDivisionError:
		return "this problem doesn't work"	
	try:
		t2 = b / a
	except ZeroDivisionError:
		return "this problem doesn't work"		
	all_ = t1 + t2
	return all_

if __name__ == "__main__":
	print(math_doer(0, 2))