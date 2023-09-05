#!/usr/bin/python3
def uppercase(str):
	for c in str.lower():
		print("{}".format(chr((ord(c) % 97) + 65) if c >= 'a' and c <= 'z' else c), end="")
	print("")
