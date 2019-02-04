#! /usr/bin/env

def sum_function(num_list):
	total = 0
	for num in num_list:
		total += num
	return total

str_num = raw_input("Please enter some numbers: ")

str_num = str_num.split()
numbers = []
for num in str_num:
	numbers.append(int(num))

sum = sum_function(numbers)
print sum
