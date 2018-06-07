import csv

txt_file = r"data_base.txt"
csv_file = r"data_base.csv"

in_txt = csv.reader(open(txt_file, "r"), delimiter = '\t')
out_csv = csv.writer(open(csv_file, 'w'))

out_csv.writerows(in_txt)