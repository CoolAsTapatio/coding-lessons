# Untitled.py
# Created by Kids on 9/30/21.
import time
fibo_results = {}
def fibonacci(n):
	if n == 1 or n == 0:
		return 1
	else:
		answer = fibonacci(n-1) + fibonacci(n-2)
		return answer
		
def memo_fibo(n):
	global fibo_results
	if n == 1 or n == 0:
		return 1
	else:
		if n in fibo_results:
			return fibo_results[n]
		else:		
			answer = fibonacci(n-1) + fibonacci(n-2)
			fibo_results[n] = answer
		return answer

def unitest_runner():
	unitest_1()
	unitest_2()

def unitest_1():
	expected = 102334155
	t0 = time.time()
	result = memo_fibo(39)
	t1 = time.time()
	assert(expected == result)
	print(t1 - t0)
	print("113")
def unitest_2():
	expected = 102334155
	t0 = time.time()
	result = fibonacci(39)
	t1 = time.time()
	assert(expected == result)
	print(t1-t0)
	print("213")
if __name__ == "__main__":
	unitest_runner()
	
'''
4 5 6  7  8  9  10 11  12  13  14  15  16   17   18   19   20    21
5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765 10946 17711
'''