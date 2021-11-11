# Untitled 2.py
# Created by Kids on 10/7/21.

class term:
	def __init__(self, coefficient, power):
		self.coefficient = coefficient
		self.power = power
	def print_term(self):
		print(str(self.coefficient) + "x^" + str(self.power))
	def evaluate(self, x):
		return self.coefficient*(x**self.power)
	def derivative(self):
		self.coefficient = self.coefficient*self.power
		self.power -= 1
		self.print_term()
	def n_derivative(self, n):
		while n > 0:
			self.derivative()
			n -= 1
if __name__ == "__main__":
	onerm = term(2, 9)
	result = onerm.evaluate(2)
	onerm.n_derivative(18)
#	onerm.print_term()
#	onerm.derivative()
#	onerm.derivative()
#	onerm.derivative()
	#print(result)