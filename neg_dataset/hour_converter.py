import csv
import sys
from random import randint


ifile = open(sys.argv[1], 'rt')
reader = csv.reader(ifile)
ofile  = open(sys.argv[2], "wt")
writer = csv.writer(ofile, delimiter=',')

rand = ['RUSH HOUR', 'AM', 'PM']
# RUSH HR = 1
# AM = 2
# PM = 3
rand_2 = [1,2,3]
for row in reader:
	#print(row[2].split(':cq')[0])
	if row[2].split(':')[0]>='12' and row[2].split(':')[0]<='15': 
		row[2] = 'PM'
		row[2] = 3
	elif row[2].split(':')[0]>='19' and row[2].split(':')[0]<='23': 
		row[2] = 'PM'
		row[2] = 3
	elif row[2].split(':')[0]>='7' and row[2].split(':')[0]<='9':
		row[2] = 'RUSH HOUR'
		row[2] = 1
	elif row[2].split(':')[0]>='16' and row[2].split(':')[0]<='18':
		row[2] = 'RUSH HOUR'
		row[2] = 1
	elif row[2].split(':')[0]>='10' and row[2].split(':')[0]<='11':
		row[2] = 'AM'
		row[2] = 2
	elif row[2].split(':')[0]>='0' and row[2].split(':')[0]<='6':
		row[2] = 'AM'
		row[2] = 2
	else:
		row[2] = row[2]
		row[2] = randint(1,3)
	writer.writerow(row)


ifile.close()
ofile.close()