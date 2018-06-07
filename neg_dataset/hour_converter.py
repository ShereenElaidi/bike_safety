import csv
import sys
import random

ifile = open(sys.argv[1], 'rt')
reader = csv.reader(ifile)
ofile  = open('data_base_converted.csv', "wt")
writer = csv.writer(ofile, delimiter=',')

rand = ['RUSH HOUR', 'AM', 'PM']
for row in reader:
	#print(row[3].split(':')[0])
	if row[2]=='':
		row[2] = random.choice(rand)
	if row[2].split(':')[0]>='12' and row[2].split(':')[0]<='15':
		row[2] = 'PM'
	if row[2].split(':')[0]>='18' and row[2].split(':')[0]<='23':
		row[2] = 'PM'
	if row[2].split(':')[0]>='7' and row[2].split(':')[0]<='8':
		row[2] = 'RUSH HOUR'
	if row[2].split(':')[0]>='16' and row[2].split(':')[0]<='17':
		row[2] = 'RUSH HOUR'
	if row[2].split(':')[0]>='9' and row[2].split(':')[0]<='11':
		row[2] = 'AM'
	if row[2].split(':')[0]>='0' and row[2].split(':')[0]<='6':
		row[2] = 'AM'
	if row[2].split(':')[0]=='9':
		row[2] = 'AM'
	
	writer.writerow(row)


ifile.close()
ofile.close()