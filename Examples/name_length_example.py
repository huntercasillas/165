#! /usr/bin/env python

first_name = raw_input("First name: ")
last_name = raw_input("Last name: ")

first_len = len(first_name)
last_len = len(last_name)

if first_len > last_len:
	print "Your first name is longest"
elif last_len > first_len:
	print "Your last name is longest"
else:
	print "Your names are the same length"
