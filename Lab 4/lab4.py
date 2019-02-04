#!/usr/bin/env python
import sys

def getLength(var1):
	length = 0
	for num in var1:
		length = length + 1
	return length

def getCount(var1, var2):
	count = 0
	for num in var1:
		if num == var2:
			count = count + 1
	return count

def createOutput(var1):
	percent = float(getCount(var1, "A")) / float(getLength(var1)) * 100	
	percentA = "(" + str(percent) + "%)"
	percent = float(getCount(var1, "C")) / float(getLength(var1)) * 100
	percentC = "(" + str(percent) + "%)"
	percent = float(getCount(var1, "G")) / float(getLength(var1)) * 100
	percentG = "(" + str(percent) + "%)"
	percent = float(getCount(var1, "T")) / float(getLength(var1)) * 100
	percentT = "(" + str(percent) + "%)"

	output = str(getLength(var1)) + '\t' + str(getCount(var1, "A")) + percentA + '\t' + str(getCount(var1, "C")) + percentC + '\t' + str(getCount(var1, "G")) + percentG + '\t' + str(getCount(var1, "T")) + percentT
		
	return output

if getLength(sys.argv) != 3: 
	print "ERROR: Incorrect number of arguments"
	sys.exit()

inputFile = open(sys.argv[1], 'r')
outputFile = open(sys.argv[2], 'w')

outputFile.write("ID\tLength\tA(%A)\tC(%C)\tG(%G)\tT(%T)\n")
header = inputFile.readline()

while header != "":
	outputFile.write(header.strip()[1:] + '\t')
	seq = inputFile.readline().replace(" ", "").upper().strip()

	v1a = getCount(seq, "A")
	v1c = getCount(seq, "C")
	v1g = getCount(seq, "G")
	v1t = getCount(seq, "T")
	v1total = v1a + v1c + v1g + v1t

	if getLength(seq) != v1total:
		outputFile.write("ERROR" + "\n")
	else:
		output = createOutput(seq)
		outputFile.write(output + "\n")

	header = inputFile.readline()

inputFile.close()
outputFile.close()
