import csv
import sys
import random


ifile = open(sys.argv[1], 'rt')
reader = csv.reader(ifile)
ofile  = open(sys.argv[2], "wt")
writer = csv.writer(ofile, delimiter=',')

rand = ['RUSH HOUR', 'AM', 'PM']
for row in reader:
	#print(row[2].split(':')[0])
	if row[2].split(':')[0]>='12' and row[2].split(':')[0]<='15': 
		row[2] = 'PM'
	elif row[2].split(':')[0]>='19' and row[2].split(':')[0]<='23': 
		row[2] = 'PM'
	elif row[2].split(':')[0]>='7' and row[2].split(':')[0]<='9':
		row[2] = 'RUSH HOUR'
	elif row[2].split(':')[0]>='16' and row[2].split(':')[0]<='18':
		row[2] = 'RUSH HOUR'
	elif row[2].split(':')[0]>='10' and row[2].split(':')[0]<='11':
		row[2] = 'AM'
	elif row[2].split(':')[0]>='0' and row[2].split(':')[0]<='6':
		row[2] = 'AM'
	else:
		row[2] = row[2]
	writer.writerow(row)


ifile.close()
ofile.close()