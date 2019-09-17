#this script reads all the lines in a file, and returns them in a list
#it also has a second function that does the opposite

from pages.colour import *

def readfile(directory):
    file = open(dir + directory, 'r')
    lines = []
    for f in file.readlines(): #get all the data from the save file
        lines.append(f.strip())
    file.close()
    return lines

def writefile(directory, writelist):
    file = open(dir + directory, 'w')
    for l in range(len(writelist)):
        file.write(writelist[l] + '\n')