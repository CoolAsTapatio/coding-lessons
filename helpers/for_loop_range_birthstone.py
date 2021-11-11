print("welcome to the birstone generator.")
listgem = ["garnet", "amythist", "aquamarine", "diamond", "emerald", "pearl", "ruby", "peridot", "sapphire", "opal", "topaz", "blue zircon"]
listmonth = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]
answer = input("enter the month that you were born in please.\n")
for t in range(0, 12, 1):
	if listmonth[t] == answer:
		print("your birthstone is " + listgem[t])
print("thanks you for doing the birthstone generator")