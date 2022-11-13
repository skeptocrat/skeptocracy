import csv, sys
# v1.0
# script for creating reader-friendly version of CSV files
# recommended to read output in text editor with line wrapping

# require filename as argument
try:
    filename = sys.argv[1]
except:
    print('ERROR: Must supply filename as argument.')
    exit()

# open input and output files
infile = open(filename)
outfile = open('output.txt', 'w')

# write to output
csvreader = csv.reader(infile, delimiter=';')
for row in csvreader:
    outfile.write('\n'.join(row) + '\n')
    outfile.write('\n')

# close all open files
infile.close()
outfile.close()
