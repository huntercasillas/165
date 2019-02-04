#! /usr/bin/env python

current_age = raw_input("How old are you? ")
current_age = int(current_age)
new_age = current_age + 5
half_age = current_age / 2.0

print "In 5 you'll be: " + str(new_age) + " years old"
print "Half your age is: " + str(half_age)

input = raw_input("So now that you're " +str(new_age) + " what do you want to do?")
print input
