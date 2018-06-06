import csv
import sys

ifile = open(sys.argv[1], 'rt')
reader = csv.reader(ifile)
RH = 0
AM = 0
PM = 0

for row in reader:
	#print(row[3].split(':')[0])
	if row[3]=='RUSH HOUR': 
		RH = RH + 1
	if row[3]=='AM': 
		AM +=1
	if row[3]=='PM': 
		PM +=1
	
print ('RH = ')
print (RH)
print ('AM = ')
print ('PM = ')
ifile.close()
