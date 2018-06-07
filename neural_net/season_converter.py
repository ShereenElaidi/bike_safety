import csv
import sys
import random

file = open(sys.argv[1], 'rt')
reader = csv.reader(file)
out = open('db_converted.csv', "wt")
writer = csv.writer(out, delimiter=",")

rand = ['WINTER', 'SPRING', 'SUMMER', 'FALL']

for row in reader:
    if (row[1]=='Date'):
        row[1] == 'Date'
    elif (row[1]==''):
        row[1] = random.choice(rand)
    elif (int(row[1].split('/')[0]) >= 12 and int(row[1].split('/')[0]) <= 2):
        row[1] == 'WINTER'
    elif (int(row[1].split('/')[0]) >= 3 and int(row[1].split('/')[0]) <= 5):
        row[1] == 'SPRING'
    elif (int(row[1].split('/')[0]) >= 6 and int(row[1].split('/')[0]) <= 8):
        row[1] == 'SUMMER'
    elif(int(row[1].split('/')[0]) >= 9 and int(row[1].split('/')[0]) <= 11):
        row[1] == 'SUMMER'

    writer.writerow(row)

file.close()
out.close()