#!/usr/bin/python
import sys
import re

if __name__ == '__main__':
	argument = sys.argv
	#del argument[0]
	print('>>', format(argument))

f = open("textfile.txt", "r")

text = f.readlines()
text = re.sub(r"[^a-zA-Z\s]", "", '{}'.format(text))

print(text)

f.close()
