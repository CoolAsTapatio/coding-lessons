# Untitled 3.py
# Created by Kids on 10/28/21.
		# Untitled 3.py
		# Created by Kids on 10/13/21.
def biggest_octo(base_10):
	starter = 1
	while starter <= int(base_10):
		starter *= 16
	return starter/16
def octodecimal_to_b10(octo):
	base_ten_number = 0
	what_to_add = 1
	place_holder = 1
	for i in range(len(octo)-1, -1, -1):
		if str(octo[i]) == "0":
			base_ten_number += int(octo[i]) * place_holder
			place_holder *= 8
		elif str(octo[i]) == "1":
			base_ten_number += int(octo[i]) * place_holder
			place_holder *= 8
		elif str(octo[i]) == "2":
			base_ten_number += int(octo[i]) * place_holder
			place_holder *= 8
		elif str(octo[i]) == "3":
			base_ten_number += int(octo[i]) * place_holder
			place_holder *= 8
		elif str(octo[i]) == "4":
			base_ten_number += int(octo[i]) * place_holder
			place_holder *= 8
		elif str(octo[i]) == "5":
			base_ten_number += int(octo[i]) * place_holder
			place_holder *= 8	
		elif str(octo[i]) == "6":
			base_ten_number += int(octo[i]) * place_holder
			place_holder *= 8
		elif str(octo[i]) == "7":
			base_ten_number += int(octo[i]) * place_holder
			place_holder *= 8
		elif str(octo[i]) == "8":
			base_ten_number += int(octo[i]) * place_holder
			place_holder *= 8
		return base_ten_number
		if __name__ == "__main__":
			print(octodecimal_to_b10("32"))