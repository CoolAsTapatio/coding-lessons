# Untitled 3.py
# Created by Kids on 1/6/22.
import numpy as np
import matplotlib.pyplot as plt
ht = {"why" : 9, "wah" : 2, "what" : 0, "the" : 6.54, "heck" : 3}
#print(ht.items[1])
keys = []
values = []
for i in sorted(ht.items(), key = lambda jay: jay[1]):
	keys.append(i[0])
	values.append(i[1])	
grid = np.arange(len(values))
plt.bar(keys, values)
plt.savefig('/Users/Kids/Desktop/graph.png')
#plt.scatter(x_coord, y_coord)
#
##creating axes and title
#plt.xlabel("guitar sales")
#plt.ylabel("MONEY")
#plt.title("The Truth")
plt.show()