# A program to turn every value for count 10+ to 10.

import csv
import sys

ifile = open(sys.argv[1], 'rt')
reader = csv.reader(ifile)
ofile = open(sys.argv[2],'wt')
writer = csv.writer(ofile, delimiter=',')


for row in reader:
    if row[3] == 'Count':
        row[3] = row[3]
    elif float(row[3]) >= 10:
        row[3] = 10
    else:
        row[3] = row[3]
    writer.writerow(row)

ifile.close()
ofile.close()