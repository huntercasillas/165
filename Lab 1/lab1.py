#!/usr/bin/env python
import sys 


var1 = raw_input("Sequence 1: ")

if var1 == "": 
	print "You must enter a DNA sequence"
	sys.exit() 

var1 = var1.replace(" ","") 
var1 = var1.upper() 

v1a = var1.count("A")
v1c = var1.count("C")
v1g = var1.count("G")
v1t = var1.count("T")
v1total = v1a + v1c + v1g + v1t

if len(var1) != v1total:
	print "ERROR: Invalid DNA sequence"
	sys.exit() 

var2 = raw_input("Sequence 2: ")

if var2 == "": 
	print "You must enter a DNA sequence"
	sys.exit() 

var2 = var2.replace(" ","") 
var2 = var2.upper() 

v2a = var2.count("A")
v2c = var2.count("C")
v2g = var2.count("G")
v2t = var2.count("T")
v2total = v2a + v2c + v2g + v2t

if len(var2) != v2total:
	print "ERROR: Invalid DNA sequence"
	sys.exit() 

var3 = raw_input("Sequence 3: ")
if var3 == "": 
	print "You must enter a DNA sequence"
	sys.exit() 

var3 = var3.replace(" ","") 
var3 = var3.upper() 

v3a = var3.count("A")
v3c = var3.count("C")
v3g = var3.count("G")
v3t = var3.count("T")
v3total = v3a + v3c + v3g + v3t

if len(var3) != v3total:
	print "ERROR: Invalid DNA sequence"
	sys.exit() 


vartotal = var1 + var2 + var3
varlength = len(vartotal)
numg = vartotal.count("G")
numc = vartotal.count("C")


print "Sequence 1:", len(var1)
print "Sequence 2:", len(var2)
print "Sequence 3:", len(var3)
print vartotal
print float(numg + numc) / varlength * 100
