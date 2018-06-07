import csv
import sys

ifile = open(sys.argv[1], 'rt')
reader = csv.reader(ifile)
ofile = open('seasons.csv', "wt")
writer = csv.writer(ofile, delimiter=',')


for row in reader:
    row[1] = row[1].split('/')[0]
    writer.writerow(row)

ifile.close()
ofile.close()