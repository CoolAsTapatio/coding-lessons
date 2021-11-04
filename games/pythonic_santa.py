# Untitled.py
# Created by Kids on 11/21/20.
import math					
def pythonic_santa(num_presents, elves, round_=1, half=0):
	print("round: ", round_)
	print("we're in half ", half)
	print(num_presents)
	if num_presents == 1:
		elves = elves + 1
		print("base case of round ", round_)
		return elves
	else:
		first_half = pythonic_santa(math.ceil(num_presents / 2), elves, round_+1, half=1)
		print("first half takes ", first_half)
		print("between 1a2")
		second_half = pythonic_santa(math.floor(num_presents / 2), elves, round_+1, half=2)
		print("second half takes", second_half)
		return first_half + second_half
if __name__ == "__main__":
	print(pythonic_santa(4, 0))
'''													15 (1)
										7								8 (2)
						3						4			4					4 (4)
					1		2				2		2	2		2			2			2    (8)
						1		1		1	 1	  1   11   1    1 1        1   1        1  1 (14)
						
						
						9
					4							5
				2			2			2			3
			1		1	1		1	1		1	2		1
											1		1'''