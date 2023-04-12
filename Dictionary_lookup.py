def main(data): # this function also know as the driver, has a run loop to execute the users commands
	print("there are " + str(len(data)) + " pieces of data")
	list_of_responses = ""
	done = False
	while done == False:
		request = input("what would you like to search from: ")
		if request == "exit":
			exit()
		elif request == "lookup":
			print(lookup_parser(data, request))
		else:
			list_of_responses = character_parser(data, request)
			print((list_of_responses))
def lookup_parser(data, request): #this function prints out the document based on its title, if the title isn't valid, it returns an error statement
	is_title_valid = False
	document = input("what would you like to lookup: ")
	for i in data:
		if document == i:
			is_title_valid = True
	if is_title_valid:
		return data[document]
	else:
		return "Error: that  is not a valid entry"
def character_parser(data, request): #this function parses a case where a user enters characters (eventually keywords), and the list of documents that the characters/key words are founds are found in
	found_titles = ""
	for i in data:
		if request in data[i]:
			found_titles += ", "
			found_titles += str(i)
	found_titles = found_titles[2: ]
	return found_titles

if __name__ == "__main__":
	title1 = "hi"
	document1 = "my name is, charles how do you do?"
	title2 = "Cyndi"
	document2 = "girls just wanna have fun"
	data_set = {title1 : document1, title2 : document2} #the title of a document and the pieces of it
	v = main(data_set)
	print(v)