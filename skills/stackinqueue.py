# Untitled.py
# Created by Kids on 12/2/21.

class Stack:
	def __init__(self):
		self.data = []
		def pop(self):
			second = []
			for i in range(len(self.data, 0, -1):
				second.append(self.data[i])
			second = second[1: ]
			for i in range(len(self.data, 0, -1):
				second.append(self.data[i])
			self.data = second
			return
		def append(self, to_be_pushed):
			self.data.append(to_be_pushed)
			return
		def get_data(self):
			return self.data
	def unitest_for_enqueueueue():
		my_queue = Queue()
		to_be_pushed = ["hi", "how are you", "im good"]
		for i in to_be_pushed:
			my_queue.enqueue(i)
		result = my_queue.get_data()
		expected = ["hi", "how are you", "im good"]
		assert(expected == result)
	def unitest_for_enqueueueue():
		my_queue = Queue()
		to_be_pushed = ["hi", "how are you", "im good"]
		for i in to_be_pushed:
			my_queue.enqueue(i)
		result = my_queue.get_data()
		expected = ["hi", "how are you", "im good"]
		assert(expected == result)
	def unitest_for_DQ():
		my_queue = Queue()
		to_be_popped = ["hi", "how are you", "im good"]
		for i in to_be_popped:
			my_queue.enqueue(i)
		my_queue.dequeue()
		result = my_queue.get_data()
		expected = ["how are you", "im good"]
		assert(expected == result)
	def main():
		unitest_for_DQ()
		unitest_for_enqueueueue()
		return
	if __name__ == "__main__":
		main()