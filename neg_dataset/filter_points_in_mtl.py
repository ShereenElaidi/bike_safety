def point_in_poly(x,y,poly):

    n = len(poly)
    inside = False

    p1x,p1y = poly[0]
    for i in range(n+1):
        p2x,p2y = poly[i % n]
        if float(y) > min(p1y,p2y):
            if float(y) <= max(p1y,p2y):
                if float(x) <= max(p1x,p2x):
                    if p1y != p2y:
                        xints = (float(y)-p1y)*(p2x-p1x)/(p2y-p1y)+p1x
                    if p1x == p2x or float(x) <= xints:
                        inside = not inside
        p1x,p1y = p2x,p2y

    return inside


import csv
import sys
import random

ifile = open(sys.argv[1], 'r')
reader = csv.reader(ifile, delimiter=',')
ofile  = open(sys.argv[2], "wt")
writer = csv.writer(ofile, delimiter=',')

polygon = [(45.70138,-73.48171),(45.65436,-73.58161),(45.57103, -73.66127),(45.50851,-73.76237),
(45.5132,-73.84494),(45.47024,-73.87653),(45.43652,-73.97129),(45.4029, -73.94966),
(45.44471,-73.79241),(45.41598, -73.61835),(45.45374, -73.56548),(45.59348,-73.51021)]


for row in reader:
    if not row: continue
    L = []
    #print(row[1])
    if (point_in_poly(row[0],row[1],polygon) == True):
        L.append(row[0])
        L.append(row[1])
        writer.writerow(L)


ifile.close()
ofile.close()






