#! /usr/bin/env python

vcf_file = open("/fslgroup/fslg_BIO165/test.vcf", "r")

for var_line in vcf_file:
	if var_line[0] != "#":
		var_line = var_line.strip()
		columns = var_line.split("\t")
		if columns[6] == "PASS":
			print var_line
vcf_file.close()

vcf_file = open("/fslgroup/fslg_BIO165/test.vcf", "r")
for var_line in vcf_file:
	var_line = var_line.strip()
	columns = var_line.split("\t")
	if var_line[0] == "#":
		print var_line
	elif columns[6] == "PASS":
		print var_line

vcf_file.close()
