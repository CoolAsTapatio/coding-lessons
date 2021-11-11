
def main():
	given_list_input = str(input("what elements (separated by a comma and a space) would you like to have printed?\n"))
	given_list = given_list_input.split(", ")
	list_printer(given_list)
def list_printer(given_list):
	for i in given_list:
		print(i)
	return
if __name__ == "__main__":
	main()
