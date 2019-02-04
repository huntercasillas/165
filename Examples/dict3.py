#! /usr/bin/env python

def load_dict(file_name):
	infile = open(file_name, "r")
	sequences = {}
	line = infile.readline()
	while line != "":
		line = line.strip()
		title = line
		line = infile.readline()
		line = line.strip()
		sequences[title] = line
		line = infile.readline()
	infile.close()
	return sequences

seq = load_dict("../practice/fasta1.fasta")

infile2 = open("../practice/fasta2.fasta", "r")
outfile = open("combined_fasta.fasta", "w")

line = infile2.readline()
while line != "":
	title = line.strip()
	line = infile2.readline()
	sequence = line.strip()
	new_seq = seq[title] + sequence
	outfile.write(title + "\n")
	outfile.write(new_seq + "\n")
	line = infile2.readline()

infile2.close()
outfile.close()







