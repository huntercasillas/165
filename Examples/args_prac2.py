#! /usr/bin/env python

import sys

def sum_function(number_list):
	total = 0
	for number in number_list:
		total += number
	return total

if len(sys.argv) == 1:
	print "You didn't enter any numbers"
else:
	numbers = []
	for number in sys.argv[1:]:
		numbers.append(int(number))
	print "The sum is: " + str(sum_function(numbers))
