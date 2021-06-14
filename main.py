import csv

with open('./sangyohi.csv', 'r') as csv_file:
 csv_reader = csv.reader(csv_file)
 data = [row for row in csv_reader]
 print(data[0])