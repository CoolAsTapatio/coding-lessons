#!/usr/bin/python

print("welcome to the birstone generator.")
listgem = ["garnet", "amythist", "aquamarine", "diamond", "emerald", "pearl", "ruby", "peridot", "sapphire", "opal" "topaz", "blue zircon"]
listmonth = ["january", "february", "march", "april", "june", "july", "august", "september", "october", "november", "december"]
answer = input("enter the month that you were born in please.\n")
print
if answer == listmonth[0]:
	print(listgem[0])
if answer == listmonth[1]:
	print(listgem[1])
elif answer == listmonth[2]:
	print(listgem[2])
elif answer == listmonth[3]:
	print(listgem[3])
elif answer == listmonth[4]:
	print(listgem[4])
elif answer == listmonth[5]:
	print(listgem[5])
elif answer == listmonth[6]:
	print(listgem[6])
elif answer == listmonth[7]:
	print(listgem[7])
elif answer == listmonth[8]:
	print(listgem[8])
elif answer == listmonth[9]:
	print(listgem[9])
elif answer == listmonth[10]:
	print(listgem[10])
else:
	print(listgem[11])