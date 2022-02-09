# Untitled.py
# Created by Kids on 1/26/22.
import base64
import codecs
def f_read(file_path):
	v = ''
	with open(file_path, 'r+') as f:
		v = f.read()
		print(v)
		v = my_decode(v)
		print("the file currently reads:\n     " + str(v))
		print("----(end of file)----\n")
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
	base64_bytes = codecs.encode(to_encode, "base64")
	#ascii_encodee = to_encode.encode('utf-8')
	#base64_bytes = base64.b64encode(ascii_encodee)
	return base64_bytes
	
def my_decode(to_decode):
	retexted = codecs.decode(to_decode, "utf-8")
	#ascii_decodee = base64.b64decode(to_decode)
	#retexted = ascii_decodee.decode('utf-8')
	#print(retexted)
	return retexted
	
def main():
	file_path = '/Users/Kids/Desktop/practice.txt'
	starting_read = f_read(file_path)
	added_to_write = adder_of_stuff(file_path, starting_read)
	encoded_file = my_encode(added_to_write)
	final_write = exit_write(file_path, encoded_file)
	
if __name__ == "__main__":
	main()
	#exit_write('/Users/Kids/Desktop/practice.txt', " ")