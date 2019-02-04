#!/usr/bin/env python
import sys

inputFile = open(".:INPUT:.", 'r')
outputFile = open(".:OUTPUT:.", 'w')

header = inputFile.readline()

while header != "":
	seq = inputFile.readline().replace(" ", "").upper().strip()
	new_var = ""

	for nuc in seq:
		if nuc == 'T':
			new_var += 'U'
		if nuc == 'A':
			new_var += 'A'
		if nuc == 'G':
			new_var += 'G'
		if nuc == 'C':
			new_var += 'C'

	outputFile.write(header)
	outputFile.write(new_var + "\n")

	header = inputFile.readline()

inputFile.close()
outputFile.close()
