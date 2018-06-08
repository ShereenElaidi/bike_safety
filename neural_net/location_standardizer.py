import csv
import sys
import random import randint

ifile = open(sys.argv[1], 'rt')
reader = csv.reader(ifile)
ofile = open(sys.argv[2], 'wt')
writer = csv.writer(ofile,delimiter =',')

#standardizing each longitude and latitude value

print
