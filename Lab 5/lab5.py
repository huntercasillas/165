#!/usr/bin/env python
import sys

def calcGC(sequence):
	numG = sequence.count("G")
	numC = sequence.count("C")
	total = len(sequence)
	percent = float(numG + numC) / total * 100
	percent = str(percent) + "%"
	return percent

def revComp(sequence):
	reverse = ""
	for nuc in sequence:
		if nuc == 'A':
			reverse += 'T'
		if nuc == 'T':
			reverse += 'A'
		if nuc == 'G':
			reverse += 'C'
		if nuc == 'C':
			reverse += 'G'
	reverse = reverse[::-1]
	return reverse

def transcribe(sequence):
	transcription = sequence.replace("T", "U")
	return transcription

def translate(sequence, codons):
	seq = sequence.replace("T", "U")
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

def countNucs(sequence):	
	percent = float(sequence.count("A")) / float(len(sequence)) * 100
	percentA = "(" + str(percent) + "%)"
	percent = float(sequence.count("C")) / float(len(sequence)) * 100
	percentC = "(" + str(percent) + "%)"
	percent = float(sequence.count("G")) / float(len(sequence)) * 100
	percentG = "(" + str(percent) + "%)"
	percent = float(sequence.count("T")) / float(len(sequence)) * 100
	percentT = "(" + str(percent) + "%)"
	
	counting = str(len(sequence)) + '\t' + str(sequence.count("A")) + percentA + '\t' + str(sequence.count("C")) + percentC + '\t' + str(sequence.count("G")) + percentG + '\t' + str(sequence.count("T")) + percentT
	return counting

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

def printError():
	error = "Error: USAGE: python myprogram.py: option input.fasta output.txt" + '\n' + '\t' + "Available options:" + '\n' + '\t' + '\t' + "-g GC%" + '\n' + '\t' + '\t' + "-r reverse complement" + '\n' + '\t' + '\t' + "-s transcription" + '\n' + '\t' + '\t' + "-t translation" + '\n' + '\t' + '\t' + "-c count nucleotides" + '\n'
	print error

def errorCheck():
	infile_name = ""
	outfile_name = ""
	codonfile_name = ""
	option = ""
	if len(sys.argv) < 4 or len(sys.argv) > 5: 
		printError()
		sys.exit()

	elif sys.argv[1] not in ['-g', '-r', '-s', '-t', '-c']:
		printError()
		sys.exit()
	else:
		if sys.argv[1] == '-t' and len(sys.argv) == 5:
			option = sys.argv[1]
			infile_name = sys.argv[2]
			codonfile_name = sys.argv[3]
			outfile_name = sys.argv[4]
		elif sys.argv[1] != '-t' and len(sys.argv) == 4:
			option = sys.argv[1]
			infile_name = sys.argv[2]
			outfile_name = sys.argv[3]
		else:
			printError()
			sys.exit()
	return infile_name, outfile_name, codonfile_name, option

def dnaCheck(sequence):
	nucA = sequence.count("A")
	nucC = sequence.count("C")
	nucG = sequence.count("G")
	nucT = sequence.count("T")
	total = nucA + nucC + nucG + nucT

	if len(sequence) != total:
		return False
	else:
		return True


infile_name, outfile_name, codonfile_name, option = errorCheck()

inputFile = open(infile_name, 'r')
codons = {}
if option == '-t':
	codons = makeDict(codonfile_name)
outputFile = open(outfile_name, 'w')


if option == '-g':
	outputFile.write("ID" + '\t' + "GC%" + '\n')

if option == '-c':
	outputFile.write("ID" + '\t' + "Length" + '\t' + "A(%A)" + '\t' + "C(%C)" + '\t' + "G(%G)" + '\t' + "T(%T)" + '\n')


header = inputFile.readline()

while header != "":
	
	if option == '-g':	
		outputFile.write(header.strip()[1:] + '\t')
		seq = inputFile.readline().replace(" ", "").upper().strip()
		seqCheck = dnaCheck(seq)
		if seqCheck == False:
			outputFile.write("ERROR" + '\n')
		elif seqCheck == True:
			percentage = calcGC(seq)
			outputFile.write(percentage + '\n')

	if option == '-r':	
		outputFile.write(header)	
		seq = inputFile.readline().replace(" ", "").upper().strip()
		seqCheck = dnaCheck(seq)
		if seqCheck == False:
			outputFile.write("ERROR" + '\n')
		elif seqCheck == True:
			reverse = revComp(seq)
			outputFile.write(reverse + '\n')

	if option == '-s':
		outputFile.write(header)	
		seq = inputFile.readline().replace(" ", "").upper().strip()
		seqCheck = dnaCheck(seq)
		if seqCheck == False:
			outputFile.write("ERROR" + '\n')
		elif seqCheck == True:
			transcription = transcribe(seq)
			outputFile.write(transcription + '\n')

	if option == '-t':
		outputFile.write(header)
		seq = inputFile.readline().replace(" ", "").upper().strip()
		seqCheck = dnaCheck(seq)
		if seqCheck == False:
			outputFile.write("ERROR" + '\n')
		elif seqCheck == True:
			translation = translate(seq, codons)
			outputFile.write(translation + '\n')

	elif option == '-c':	
		outputFile.write(header.strip()[1:] + '\t')
		seq = inputFile.readline().replace(" ", "").upper().strip()
		seqCheck = dnaCheck(seq)
		if seqCheck == False:
			outputFile.write("ERROR" + '\n')
		elif seqCheck == True:
			counting = countNucs(seq)
			outputFile.write(counting + '\n')

	header = inputFile.readline()

inputFile.close()
outputFile.close()
