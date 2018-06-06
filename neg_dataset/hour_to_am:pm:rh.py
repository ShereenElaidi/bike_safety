import csv
import sys
import random

ifile = open(sys.argv[1], 'rt')
reader = csv.reader(ifile)
ofile  = open('ttest.csv', "wt")
writer = csv.writer(ofile, delimiter=',')

rand = ['RUSH HOUR', 'AM', 'PM']
for row in reader:
	#print(row[3].split(':')[0])
	if row[3]=='': 
		row[3] = random.choice(rand)
	if row[3].split(':')[0]>='12' and row[3].split(':')[0]<='15': 
		row[3] = 'PM'
	if row[3].split(':')[0]>='18' and row[3].split(':')[0]<='23': 
		row[3] = 'PM'
	if row[3].split(':')[0]>='7' and row[3].split(':')[0]<='8':
		row[3] = 'RUSH HOUR'
	if row[3].split(':')[0]>='16' and row[3].split(':')[0]<='17':
		row[3] = 'RUSH HOUR'
	if row[3].split(':')[0]>='9' and row[3].split(':')[0]<='11':
		row[3] = 'AM'
	if row[3].split(':')[0]>='0' and row[3].split(':')[0]<='6':
		row[3] = 'AM'
	if row[3].split(':')[0]=='9':
		row[3] = 'AM'
	
	writer.writerow(row)


ifile.close()
ofile.close()