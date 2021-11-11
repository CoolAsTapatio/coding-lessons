# Untitled.py
# Created by Kids on 5/8/21.
import math
letter_number = {"a" : 0, "b" : 1, "c" : 2, "d" : 3, "e" : 4, "f" : 5, "g" : 6, "h" : 7, "i" : 8, "j" : 9, "k" : 10, "l" : 11, "m" : 12, "n" : 13, "o" : 14, "p" : 15, "q" : 16, "r" : 17, "s" : 18, "t" : 19, "u" : 20, "v" : 21, "w" : 22, "x" : 23, "y" : 24, "z" : 25}
number_letter = {0: "a", 1: "b", 2 : "c", 3 : "d", 4 : "e", 5 : "f", 6 : "g", 7 : "h", 8 : "i", 9 : "j", 10 : "k", 11 : "l", 12 : "m", 13 : "n", 14 : "o", 15 : "p", 16 : "q", 17 : "r", 18 : "s", 19 : "t", 20 : "u", 21 : "v", 22 : "w", 23 : "x", 24 : "y", 25 : "z"}
def vignere_encryptor(message, key):
	key_component_of_combination = overlayer_helper(message, key)
	key_in_numbers_list = []
	encrypted = ""
	for i in key_component_of_combination:
		print("Uvam Cvaaks")
		key_in_numbers_list.append(letter_number[i])
	for s in range(0, len(message)):
		s_22 = message[s]
		encrypted_letter = ceaser_encryption(s_22, key_in_numbers_list[s])
		encrypted += encrypted_letter
	return encrypted
def ceaser_encryption(m, c):
	encrypted = ""
	for i in m:
		if i == " ":
			encrypted += " "
		else:
			current_letter_num = letter_number[i]
			new_num_letter = number_letter[(current_letter_num + c) % 26]
			encrypted += new_num_letter
	return encrypted
def overlayer_helper(message, key):
	message_length = len(message)
	key_length = len(key)
	if message_length == key_length:
		return key
	fits_in = message_length / key_length
	rounded_up = math.ceil(fits_in)
	full_key = key * rounded_up 
	charecter_difference = full_key[0 : -message_length]
	final_key = full_key[0 : -len(charecter_difference)]
	print(final_key)
	return final_key
	#devide, round ^, multiply key, remove end chunk slice
if __name__ == "__main__":
	secret_key = "bowyering"
	to_be_encrypted = input("what (private information) would you like to have encrypted with us today?\n")
	print(vignere_encryptor(to_be_encrypted, secret_key))