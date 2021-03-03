# Lorenzo Gonzales
# ID: 1934789
# Word Frequencies
# This program reads input from another file
# reads the file using the csv.reader() method
# outputs words and the amount of times they occur
import csv
with open('input1.csv') as csvfile:
    W_F = csv.reader(csvfile, newline='/n')

