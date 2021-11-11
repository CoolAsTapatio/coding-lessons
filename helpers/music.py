# Untitled.py
# Created by Kids on 8/21/20.

goodgenresofmusic = ["pop", "pop country", "country", "pop rock"]
badgeneresofmusic = ["disco", "heavy metal", "gospel", "rock", "ballad"]


typesofcountry = ["pop country", "rock country"]
typesofpop = ["soft pop", "pop rock"]
tyesofgospel = ["horrible", "revulsing"]
typesofrock = ["punk", "heavy metal"]
listofmusictypes = [typesofpop, typesofrock, typesofcountry, tyesofgospel]
bestmuscitype = "pop country"

for t in listofmusictypes:
	for t2 in t:
		print(t2)
		if t2 == bestmuscitype:
			print(bestmuscitype + " is the best type of music")