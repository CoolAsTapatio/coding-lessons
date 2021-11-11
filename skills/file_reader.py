# Untitled
# Created by Kids on 4/24/21.
def high_score():
	with open('high_score.txt', 'r') as f:
		read_data = f.read()
		print(read_data)
	with open('high_score.txt', 'w') as high_score_file:
		high_score_file.write('0')
if __name__ == "__main__":
	high_score()
	