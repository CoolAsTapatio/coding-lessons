#!/usr/bin/python

lista = [1,2,3,4,5,6,7,8,9,0]
#print(lista[10])
#O(a*n +1 + 1) -  O(20 + 2)    O( + 2)
def for_loop_func():
	print("hi") #O(1) - constant bec
	#+
	for_returner = [] #O(1) - constant time ---- the time it takes does NOT depend on the size of the list
	#+
	#O(a*n)
	for i in range(0, len(lista), 1):  # the for loop runs O(n) times where n is the size of the list (len(lista))
		for_returner.append(lista[i])  # append function takes O(a)
	#+
	return for_returner #O(1)
'''listb = ["theo", "zoi", "steve", "pam'"]
for s in range(0, 4, 2):
	print(listb[s])
print(len(listb))
for t in range(0, len(listb), 2):
	# if t == 0:
	# listb[0]
	if listb[t] == "theo":
		print("teooooo daaaaaaaaaaa keeeeeeeeeeeeeng fo evaaaaaaa")
	else:
		print("waaaaaaaaaaaaaaaaaaaaa")

list888888 = ["january", "february", "march", "april", "may", "june"]
for r in range(0, len(list888888), 1):
	if list888888[r] == "april":
		print("april showers")
	elif list888888[r] == "may":
		print("bring may flowers")
	else:
		print("too hot or too cold")


sub0 = "math"
sub1 = "science"
sub2 = "social studies"
sub3 = "la ugh"




listc = [sub0, sub1, sub2, sub3, 24]
for s in range(0, len(listc) , 1):
	print(listc[s])'''
if __name__ == "__main__":
	print(for_loop_func())