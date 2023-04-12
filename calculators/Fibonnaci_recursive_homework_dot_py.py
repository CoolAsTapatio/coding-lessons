# Untitled.py
# Created by Kids on 8/31/22.

def fibonacci_calc(n, first_num=0, second_num=1):
	if n == 0:
		return 1
	if n == 1:
		return 1
	else:
		first_num = fibonacci_calc(n-1)
		second_num = fibonacci_calc(n-2)
		return first_num + second_num

if __name__ == "__main__":

	n_fibo_num = int(input("what fibonacci number would you like to have returned?\n")) - 1
	print(fibonacci_calc(n_fibo_num))