# Lorenzo Gonzales
# ID: 1934789
# Zylabs 11.22 CIS 2348 LAB: Word frequencies
# This program reads a list of words. Then, the program outputs those words and their frequencies.
my_words = list(input().split()) # User inputs string values to be counted, split function is used to separate values when inputted as individual elements
for W_C in range(0, len(my_words)): # for condition is created to read length of strings, W_C is assigned as i value abbreviated for word count
    print(my_words[W_C], my_words.count(my_words[W_C])) # program prints out strings and the amount of occurrences the words are used


