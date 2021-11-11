# Untitled 3.py
# Created by Kids on 10/13/21.
def biggest_hexi(base_10):
	starter = 1
	while starter <= int(base_10):
		starter *= 16
	return starter/16
def hexidecimal_to_b10(hexi):
	base_ten_number = 0
	what_to_add = 1
	place_holder = 1
	for i in range(len(hexi)-1, -1, -1):
		if str(hexi[i]) == "0":
			base_ten_number += int(hexi[i]) * place_holder
			place_holder *= 16
		elif str(hexi[i]) == "1":
			base_ten_number += int(hexi[i]) * place_holder
			place_holder *= 16
		elif str(hexi[i]) == "2":
			base_ten_number += int(hexi[i]) * place_holder
			place_holder *= 16
		elif str(hexi[i]) == "3":
			base_ten_number += int(hexi[i]) * place_holder
			place_holder *= 16
		elif str(hexi[i]) == "4":
			base_ten_number += int(hexi[i]) * place_holder
			place_holder *= 16
		elif str(hexi[i]) == "5":
			base_ten_number += int(hexi[i]) * place_holder
			place_holder *= 16	
		elif str(hexi[i]) == "6":
			base_ten_number += int(hexi[i]) * place_holder
			place_holder *= 16
		elif str(hexi[i]) == "7":
			base_ten_number += int(hexi[i]) * place_holder
			place_holder *= 16
		elif str(hexi[i]) == "8":
			base_ten_number += int(hexi[i]) * place_holder
			place_holder *= 16
		elif str(hexi[i]) == "9":
			base_ten_number += int(hexi[i]) * place_holder
			place_holder *= 16
		elif str(hexi[i]) == "a":
			base_ten_number += 10 * place_holder
			place_holder *= 16
		elif str(hexi[i]) == "b":
			base_ten_number += 11 * place_holder
			place_holder *= 16					
		elif str(hexi[i]) == "c":
			base_ten_number += 12 * place_holder
			place_holder *= 16	
		elif str(hexi[i]) == "d":
			base_ten_number += 13 * place_holder
			place_holder *= 16
		elif str(hexi[i]) == "e":
			base_ten_number += 14 * place_holder
			place_holder *= 16		
		elif str(hexi[i]) == "f":
			base_ten_number += 15 * place_holder
			place_holder *= 16	
		elif str(hexi[i]) == "g":
			base_ten_number += 16 * place_holder
			place_holder *= 16	
	return base_ten_number
if __name__ == "__main__":
	print(hexidecimal_to_b10("1a3ab"))