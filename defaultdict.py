from collections import defaultdict

periodic_table = {'Hydrogen': 1, 'Helium': 2}
print(periodic_table)

carbon = periodic_table.setdefault('Carbon', 12)
print(periodic_table)

periodic_table = defaultdict(int)
print(periodic_table)

periodic_table['Hydrogen'] = 1
periodic_table['Lead']
print(periodic_table)

def nothing():
    return 'Empty'

strdict = defaultdict(nothing)
print(strdict)
strdict['A'] = 'aaaa'
strdict['B'] = 'bbbb'
strdict['C']
print(strdict)