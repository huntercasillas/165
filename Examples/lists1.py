#! /usr/bin/env python

s1 = "AAGGTGGACG"
s2 = "CGCCGGTTGGAC"
s3 = "AAATGGACCCGTACGTGGTGTGGG"

dna_list = [s1, s2, s3]
dna_list.sort()

print dna_list
print "\n".join(dna_list)
