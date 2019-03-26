# This is a work by
# Vitalijs Smirnovs
# Stydent ID # g00317774

# Problem 9: Write a program that reads in a text file and outputs evry secondline. 
# The program should take the filename from an argument on the command line. 
# open a text file, save as openfile
# openfile = open('theinvisibleman.txt')

# to read filename from a command line:
# import sys
import sys

# to read in file from a command line as an argument 2
openfile = open(sys.argv[1])
lines = openfile.readlines()
# count number of lines
# from https://www.sanfoundry.com/python-program-count-lines-text-file/
linecount = 0
for line in lines:
    linecount += 1
    
openfile.close()

# to print every second line, start with line 2
i=2

# while counter is less or equal number lines, print every second line
for each in lines:
    while i<=linecount:
        print(lines[i])
        i=i+2