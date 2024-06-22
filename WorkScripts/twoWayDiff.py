#This script is for finding matches between two files scanning both files against each other

#import csv module
import csv

#instantiate both files using the open module
with open('<filename>', 'r') as f1, open('<filename2>', 'r') as f2:
    f1_lines = f1.readlines()
    f2_lines = f2.readlines()

#use open module to iterate through lists and create output file
with open('<outputfilename>', 'w') as difference_file:
    for line in f1_lines:
        if line not in f2_lines:
            difference_file.write(line)
    for line in f2_lines:
        if line not in f1_lines:
            difference_file.write(line)