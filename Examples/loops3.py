#! /usr/bin/env python

num_seq = raw_input("Number sequences: ")
num_seq = int(num_seq)

sequences = []
count = 0
while count < num_seq:
	seq = raw_input("Sequence: ")
	seq = seq.upper()
	sequences.append(seq)
	count += 1
sequences.sort()
print "\n".join(sequences)
print ""

sequences = []
for number in range(num_seq):
	seq = raw_input("Sequence: ")
	seq = seq.upper()
	sequences.append(seq)
sequences.sort()
print "\n".join(sequences)






