import re
source = 'ooiaeo naknfdafea'
n = re.match('ooi', source)

if n:
    print(n.group())

n = re.match('OOI', source)

if n:
    print(n.group())

n = re.search('nfd', source)

if n:
    print(n.group())

n = re.search('.*aeo', source)

if n:
    print(n.group())

n = re.findall('a', source)
print(n)
print('Found', len(n), 'matches')

n = re.findall('.a..', source)
print(n)

# 맨 끝 a 찾기
n = re.findall('a.?', source)
print(n)

n = re.split('a', source)
print(n)

# 바꾸기
n = re.sub('a', 'A', source)
print(n)
