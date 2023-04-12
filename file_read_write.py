# Untitled.py
# Created by Kids on 1/26/22.
import base64
def f_read(file_path):
	v = ''
	with open(file_path, 'r+') as f:
		v = f.read()
		print(v)
		v = my_decode(v)
		print("the file currently reads:\n     " + str(v))
		print("----(end of file)----\n")
		print("v: " + v)
		return v
		
def adder_of_stuff(file_path, starting_read):
	return str(starting_read) + "\n\n" + input('what should i add?\n')
	
def exit_write(file_path, encoded):
	with open(file_path, 'w+') as w:
		w.write(str(encoded))
		return
		'''
		encoding:  plaintext --> ascii --> base64
						var.encode()  b64encode()
		'''
				
def my_encode(to_encode):
	utf8_bytes = to_encode.encode()
	base64_bytes = base64.b64encode(utf8_bytes)
	return base64_bytes
	
def my_decode(to_decode):
#	to_decode = "b'bG9zdCBpbiB0cmFuc2xhdGlvbg=='"
	retexted = base64.b64decode(to_decode)
	retexted = retexted.decode()
	return retexted
	
def main():
	file_path = '/Users/Kids/Desktop/practice.txt'
	tester_ = 'lost in translation'
	encoded_file = my_encode(tester_)
	final_write = exit_write(file_path, encoded_file)
	starting_read = f_read(file_path)
	print("starting read is: " + starting_read)
	decoded_stuff = my_decode(starting_read[2: -1])
	print(decoded_stuff)
	#added_to_write = adder_of_stuff(file_path, starting_read)

	
if __name__ == "__main__":
	exit_write('/Users/Kids/Desktop/practice.txt', " ")
	main()
	