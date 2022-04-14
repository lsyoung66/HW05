#!/usr/bin/python
import sys
import re

if __name__ == '__main__':
        f = open(sys.argv[1], "r")
        num = int(sys.argv[2])

        line = f.readlines()
        
        f.close()

        word = []
        D = {}

        for i in range(0, len(line)):
                word.extend(line[i].split())
                
        line = re.sub(r"[^a-zA-Z\s]", "", '{}'.format(line))

        for i in range(0, len(word)):
                if word[i] in D:
                        D[word[i]] += 1
                else:
                        D[word[i]] = 1

        D_desc = sorted(D.items(), key=lambda x: x[1], reverse=True)

        for i in range(0, num):
                          print("{0:<20}{1:<20}".format(D_desc[i][0], D_desc[i][1]))
