# Untitled.py
# Created by Kids on 8/25/20.

Lista = ["awesome", "cool", "amazing"]
Listb = ["mild",  "not great"]
Listc = ["sulky", "horrible", "atrocious"]
Listall = [Lista, Listb, Listc]
'''
for o in Listall:
	print(o)
	for o2 in o:
		print(o2)
'''
for o in range(0,len(Listall), 1):
	#for o2 in Listall[o]:
		
	#	print(o2)
	for o2 in range(0, len(Listall[o]), 1):
		#print(Listall[o])
		pass		
list8 = [Listall, Listc]
print(list8[0][0][0])
for i in range(0, len(list8), 1):
	for i2 in (0, len(i), 1):
		print(list8[i2])