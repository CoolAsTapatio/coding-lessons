# Untitled.py
# Created by Kids on 4/27/22.
# clarifying questions
#
#
# nums = [2,7,11,15]
# target = 9
# output: [0,1]
#
#
#
def main(target_number, list_of_numbers):
	ht_ = {}	
	for t in range(len(list_of_numbers)):
		ht_[list_of_numbers[t]] = t
	for i in ht_:
		if target_number - i in ht_:
			return ht_[i], ht_[target_number-i]
if __name__ == "__main__":
	print(main(9, [2,7,11,15]))