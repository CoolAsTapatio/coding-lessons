# Untitled.py
# Created by Kids on 12/2/21.
class Queue:
	def __init__(self):
		self.data = []
	def dequeue(self):
		to_return = self.data[0]
		self.data = self.data[1: ]
		return = to_return
	def enqueue(self, to_be_pushed):
		self.data.append(to_be_pushed)
		return
	def get_data(self):
		return self.data
class Stack:
	def __init__(self):
		self.data = []
	def pop(self):
		to_return = self.data[0]
		self.data = self.data[1: ]
		return to_return
	def push(self, to_be_pushed):
		self.data.append(to_be_pushed)
		return
	def get_data(self):
		return self.data
class Queue_using_Stack:
	def __init__(self):
		self.stack = Stack()
	def enqueue(self, to_push):
		place_saver = []
		for i in range(len(self.stack.data), 0, -1):
			place_saver.append(self.stack.pop())
		self.stack.data = place_saver
		self.stack.push(to_push)
		place_saver = []
		for i in range(2, len(self.stack.data), 1):
			place_saver.append(self.stack.push())
		self.stack.data = place_saver
		return
	def dequeue(self):
		self.stack.pop()
		return
def main():
	
	return
if __name__ == "__main__":
	main()
	
'''
to push = d
[a, b, c]
[0, a, b, c]
insert d(1)
list = list[1: ]
'''