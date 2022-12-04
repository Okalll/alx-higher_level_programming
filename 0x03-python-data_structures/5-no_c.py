#!/usr/bin/python3
def no_c(my_string):

	n_string = ""
	for i in range(len(my_string)):
	if my_string[i] != 'c' and my_string[i] != 'C':
		n_string += my_string[i]
	return n_string
