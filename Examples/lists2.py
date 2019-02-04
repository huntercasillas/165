#! /usr/bin/env python

seq = raw_input("Sequence: ")
positions = raw_input("positions: ").split()

pos1 = int(positions[0])
pos2 = int(positions[1])

exon1 = seq[0:pos1]
exon2 = seq[pos2 - 1:]

print exon1 + exon2
