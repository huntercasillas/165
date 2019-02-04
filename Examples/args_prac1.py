#! /usr/bin/env python

import sys

infile = open(sys.argv[1], "r")
outfile = open(sys.argv[2], "w")
gene = sys.argv[3].upper()

for line in infile:
	if line[0] == "#":
		outfile.write(line)
	elif gene in line.upper():
		outfile.write(line)
infile.close()
outfile.close()
