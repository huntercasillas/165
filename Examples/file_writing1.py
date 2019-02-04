#! /usr/bin/env python

infile = open("/fslgroup/fslg_BIO165/test.vcf", "r")
outfile = open("test_out.vcf", "w")

line = infile.readline()
while line[0] == "#":
	outfile.write(line)
	line = infile.readline()

while line != "":
	line = line.strip()
	cols = line.split("\t")
	if cols[6] == "PASS":
		line = line.replace("PASS", "pass")
		outfile.write(line + "\n")
	line = infile.readline()
infile.close()
outfile.close()
