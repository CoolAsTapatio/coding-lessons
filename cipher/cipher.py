# Untitled 2.py
# Created by Kids on 5/11/21.

letter_number = {"a" : 0, "b" : 1, "c" : 2, "d" : 3, "e" : 4, "f" : 5, "g" : 6, "h" : 7, "i" : 8, "j" : 9, "k" : 10, "l" : 11, "m" : 12, "n" : 13, "o" : 14, "p" : 15, "q" : 16, "r" : 17, "s" : 18, "t" : 19, "u" : 20, "v" : 21, "w" : 22, "x" : 23, "y" : 24, "z" : 25}
number_letter = {0: "a", 1: "b", 2 : "c", 3 : "d", 4 : "e", 5 : "f", 6 : "g", 7 : "h", 8 : "i", 9 : "j", 10 : "k", 11 : "l", 12 : "m", 13 : "n", 14 : "o", 15 : "p", 16 : "q", 17 : "r", 18 : "s", 19 : "t", 20 : "u", 21 : "v", 22 : "w", 23 : "x", 24 : "y", 25 : "z"}
'''def encryption_iteration(m, count=0):
	if count == 25:
		return "done"
	else:
		encrypted = ""
		for i in m:
			if i == " ":
				encrypted += " "
			else:
				current_letter_num = letter_number[i]
				new_num_letter = number_letter[(current_letter_num + count) % 26]
				encrypted += new_num_letter
		print(encrypted + " the key is " + str(count))
		return encryption_iteration(m, count + 1)'''
def decryption(m, c, o):
	encrypted = ""
	for i in m:
		if i == " ":
			encrypted += " "
		else:
			current_letter_num = letter_number[i]
			new_num_letter = number_letter[(current_letter_num + c) % 26]
			encrypted += new_num_letter
			if c < 25:
				c % 26 
			else:
				c += o
	return encrypted

if __name__ == "__main__":
	to_be_encrypted = input("the ceaser cipher is so simple.")
	print(decryption(to_be_encrypted, 5, 3))
