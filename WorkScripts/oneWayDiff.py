#This script was written to find differences between two csv files based on a
#text string using the csv module

#import csv module
import csv

#use open method to instantiate both files
with open('<filename>', 'r') as f1, open('<filename2>', 'r') as f2:
    f1_lines = f1.readlines()
    f2_lines = f2.readlines()

#use open method to iterate through both files looking for matches
#Write non-matches to new file
with open('<outputfilename>', 'w') as difference_file:
    for line in f1_lines:
        if line not in f2_lines:
            difference_file.write(line)