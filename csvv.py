import csv
data = [['a', 'b', 'c'], ['qq', 'ww', 'ee'], ['pp', 'oo']]

with open('csvdata', 'wt') as fout:
    csvout = csv.writer(fout)
    csvout.writerows(data)