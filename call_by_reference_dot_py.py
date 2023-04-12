# Untitled 2.py
# Created by Kids on 8/25/22.
def main(v, d):
	v += 1
	d -= 1
	return v, d

if __name__ == "__main__":
	v = 1
	d = 3
	print("v = " + str(v) + " and d = " + str(d))
	v,d = main(v, d)
	print("v = " + str(v) + " and d = " + str(d))