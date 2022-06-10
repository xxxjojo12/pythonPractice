import csv
with open('csvdata', 'rt') as fin:
    cin = csv.reader(fin)
    data = [row for row in cin]

print(data)