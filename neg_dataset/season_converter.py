import csv
import sys
import random


ifile = open(sys.argv[1], 'rt')
reader = csv.reader(ifile)
ofile  = open(sys.argv[2], "wt")
writer = csv.writer(ofile, delimiter=',')

rand = ['SPRING', 'SUMMER', 'FALL', 'WINTER']
for row in reader:
	#print(row[2].split(':')[0])
	row[1] = row[1].split('/')[0] 
	writer.writerow(row)

ifile.close()
ofile.close()