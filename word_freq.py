#!/usr/bin/python
import sys
import re

if __name__ == '__main__':	
	f = open("sys.argv[1]", "r")
	num = int(sys.argv[2])

	line = f.readlines()
	line = re.sub(r"[^a-zA-Z\s]", "", '{}'.format(line))

	f.close()
	
	D = {}
	
	for i in range(0, len(line)):
		word.extend(line[i].split())
		
	for i in range(0, len(word)):
		if word[i] in D:
			D[word[i]] += 1
		else:
			D[word[i] = 1
	
	D_desc = sorted(D.items(), key=lambda x: x[1], reverse=True)
			  
	for i in range(0, num):
			  print("%-20s@20d" % '{}'.format(D_desc))
	
