import csv
import sys
import random

ifile = open(sys.argv[1], 'r')
reader = csv.reader(ifile, delimiter=',')
ofile  = open(sys.argv[2], "wt")
writer = csv.writer(ofile, delimiter=',')


for row in reader:
	if not row: continue
	L = []
	#print(row[1])
	L.append(row[1])
	L.append(row[3])
	writer.writerow(L)


ifile.close()
ofile.close()