import csv
import sys
import random


ifile = open(sys.argv[1], 'rt')
reader = csv.reader(ifile)
ofile  = open(sys.argv[2], "wt")
writer = csv.writer(ofile, delimiter=',')
rand_year = ['2006', '2007', '2008', '2009', '2010']
rand_day = list(range(1,29))
rand_month = list(range(1,13))
rand_time = ['RUSH HOUR', 'AM', 'PM']

writer.writerow(['Year', 'Date', 'Time', 'Count', 'Lat', 'Lng'])
for row in reader:
	result = []
	year = str(random.choice(rand_year))
	month = str(random.choice(rand_month))
	day = str(random.choice(rand_day))
	time = str(random.choice(rand_time))
	result.append(year)
	result.append((month + '/' + day + '/' + year[2:]))
	result.append(time)
	result.append(0.0)
	result.append(row[0])
	result.append(row[1])
	#result = [year] + [month + '/' + day + '/' + year[2:]] + [time] + [0.0] + row[0] + row[1]
	writer.writerow(result)


ifile.close()
ofile.close()