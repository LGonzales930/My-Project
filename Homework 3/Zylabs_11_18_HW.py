# Lorenzo Gonzales
# ID: 1934789
# Zylabs 11.18 CIS 2348LAB: Filter and Sort a list
# This program gets a list of integers from input, and outputs non-negative integers in ascending order (lowest to highest)
my_nums = list(int(input()).split())  # User inputs multiple integers to start the program
num_list = [] # empty list is created to house variables
for integers in num_list: # a condition that filters out negative integer values
    if integers > -1: # the condition stands that if the value is greater then or equal to zero
        num_list.append(integers)  # The value is then appended
num_list.sort() # Integers are sorted from lowest to highest
print(num_list)  # Program Outputs values without negative values and sorted from least to greatest
