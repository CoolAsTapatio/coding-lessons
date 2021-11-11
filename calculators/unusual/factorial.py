# Untitled 3.py
# Created by Kids on 12/12/20.
'''memo_helper = {}
def memo_factorial(n):
	if n == 1:
		memo_helper[1] = 1
		return 1
	else:
		if n in memo_helper:
			print("if")
			return memo_helper[n]
		else:
			a = n * memo_factorial(n-1)
			memo_helper[n] = a
			return a'''
def tail_fac_n(n):
	v = go_(n, 1)
	return v
def go_(n, a, count=1):
	print(count)
	if n == 1:
		return a
	else:
		return go_(n-1, a*n, count+1)
if __name__ == "__main__":
	print(tail_fac_n(1))
	