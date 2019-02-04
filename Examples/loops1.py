#! /usr/bin/env python

seq = raw_input("DNA seq: ")
seq = seq.upper()

new_seq = ""
for nuc in seq:
	if nuc == "T":
		new_seq += "U"
	elif nuc != " ":
		new_seq += nuc

print new_seq

new_seq = ""
num = 0
length = len(seq)
while num < length:
	if seq[num] == "T":
		new_seq += "U"
	elif seq[num] != " ":
		new_seq += seq[num]
	num += 1
print new_seq
	












