#!/usr/bin/env python
import sys

def translate(seq, codons):
	seq = seq.replace("T", "U")
	protein = ""
	pos = 0
	while pos < (len(seq)-2):
		codon = seq[pos:pos+3]
		aa = codons[codon]
		if aa == "*":
			break
		protein += aa
		pos += 3
	return protein

def makeDict(cfn):
	cf = open(cfn, 'r')
	d = {}
	for line in cf:
		fields = line.strip().split('\t')
		codon = fields[0]
		aa = fields[1]
		d[codon] = aa
	cf.close()
	return d

inputFile = open(".:INPUT:.", 'r')
outputFile = open(".:OUTPUT:.", 'w')

header = inputFile.readline()
dict = makeDict(".:CODON:.")

while header != "":
	seq = inputFile.readline().replace(" ", "").upper().strip()
	new_var = ""

	v1a = seq.count("A")
	v1c = seq.count("C")
	v1g = seq.count("G")
	v1t = seq.count("T")
	v1total = v1a + v1c + v1g + v1t
	
	outputFile.write(header)

	if len(seq) != v1total:
		new_var = "ERROR"
		outputFile.write(new_var + "\n")
	else:
		protein = translate(seq, dict)
		outputFile.write(protein + "\n")

	header = inputFile.readline()

inputFile.close()
outputFile.close()
