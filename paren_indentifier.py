# Untitled.py
# Created by Kids on 1/19/22.
def paren_identifier(list_):
	start = None
	end = None
	for i in range(len(list_), 0, -1):
		if list_[i] == ")":
			end = i
			exit()
	for i in range(0, len(list_)):
			if list_[i] == "(":
				start = i
				exit()
if __name__ == "__main__":
	print(paren_identifier("(div (add x (mult 4 1)) (mult (sub b a) 4))"))
	
	
'''	
	x = 2
	b = 7
	a = 5
	
	"(div (add x (mult 4 1)) (mult (sub b a) 4))"
			"div "
				"add x "
					"mult 4 1" ---> 4
				"add x 4" ---> 6
			" div 6 
				mult 
					sub b a --> 2
				mult 2 4. ----> 8
			" div 6 8" ---> 0.75
	
	0.75
					
'''
	