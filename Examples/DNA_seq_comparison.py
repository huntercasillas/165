#! /usr/bin/env python

seq1 = raw_input("Please enter a DNA sequence: ")
seq2 = raw_input("Please enter a DNA sequence: ")

seq1 = seq1.upper()
seq2 = seq2.upper()

if seq1 == seq2:
	print "Hooray, the sequences are equal!"
else:
	print "The sequences are different"
