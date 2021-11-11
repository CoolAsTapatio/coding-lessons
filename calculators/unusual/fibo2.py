# Untitled 3.py
# Created by Kids on 12/5/20.
memo_ht = {}
'''def fibo_sucks(n):
	if n == 1 or n == 0:
		return 1
	else:
		return fibo_sucks(n-1) + fibo_sucks(n-2)
		
def fibo_mss(n):
	if n == 1 or n == 0:
		return 1
	else:
		fib1 = None
		fib2 = None
		if n-1 in memo_ht:
			fib1 = memo_ht[n-1] 
		else:
			fib1 = fibo_mss(n-1)
			memo_ht[n-1] = fib1
		if n-2 in memo_ht:
			fib2 = memo_ht[n-2]
		else:
			fib2 = fibo_mss(n-2)
			memo_ht[n-2] = fib2
		the_var = fib1 + fib2
		return the_var'''
def tail_fibo(n):
	v = go(n, 1, 1)
	return v
def go(n, a, b):
	if n == 0:
		return a
	elif n == 1:
		return b
	else:
		return go(n-1, b, b+a)
if __name__ == "__main__":
	print(tail_fibo(977))