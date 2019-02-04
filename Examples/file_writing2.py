#! /usr/bin/env python

fastain = open("/fslgroup/fslg_BIO165/input.fasta", "r")
fastaout = open("fixed.fasta", "w")

line = fastain.readline()
while line != "":
	fastaout.write(line)
	line = fastain.readline()
	sequence = ""
	while line != "" and line[0] != ">":
		sequence += line.strip()
		line = fastain.readline()
	fastaout.write(sequence + "\n")

fastain.close()
fastaout.close()
