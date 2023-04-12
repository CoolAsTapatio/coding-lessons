# Untitled.py
# Created by Kids on 5/4/22.

#def my_first_generator():
#	yield 1
#	yield 2
#	yield 3
# authenticate bob ---- 1)
# authenticate joe ---- 2)
acquire(lock_b) ---- 1) P1 Acq LB
# check that bob has enough money to give joe what he wants to ---  4)
acquire(lock_a) --- Waiting

release(lock_a)
release(lock_b)

# subtract money from bob ---- 6)
# add money to joe
# release(lock_bob)
# tell bob transaction is succesful
# to joe transaction is succesful
--------------------

acquire(lock_a) ------- 2) P2 Acq LA


acquire(lock_b) -------- waiting


release(lock_b)
release(lock_a)
# authenticate bob ----3)
# authenticate sally ----
# acquire(lock_bob)
# check that bob has enough money to give sally what he wants to ----- 5)
# subtract money from bob 7)
# add money to sally
# release(lock_bob)
# tell bob transaction is succesful
# to sally transaction is succesful


	
def fibo_generator(n, first_num=0, second_num=1):
	if n == 0:
		yield 0
	if n == 1:
		yield 1
	else:
		yield from fibo_generator(n-1, second_num, first_num + second_num)

if __name__ == "__main__":
#	for y in my_first_generator():
#		print(y)
	n_fibo_num = int(input("what fibonacci number would you like to have returned?\n")) - 1
	for i in fibo_generator(n_fibo_num):
		print(i)