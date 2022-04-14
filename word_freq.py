#!/usr/bin/python
import sys
import re

if __name__ == '__main__':
	argument = sys.argv
	
f = open("sys.argv[1]", "r")
num = int(sys.argv[2])

line = f.readlines()
line = re.sub(r"[^a-zA-Z\s]", "", '{}'.format(line))

f.close()
