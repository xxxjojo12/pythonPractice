# Tuple
a = (1, 2, 'a', (3, 4), 5)
# del a[0]
print(a[0:3])
print(a[4])

print('--------------------------------------')

# Dictionary (key : value) -> items
b = {
    'Hail' : 1,
    'Lim' : 2,
    'age' : 29
}
print(b['age'])
b['old'] = 30
print(b)

del b['Lim']
print(b)

print(b.keys())
print(b.values())

print(b.items())

print(b.clear())

# Two lists into one dictionary
l1 = ['apple', 'banana', 'orange']
l2 = [1, 2, 3]
d1 = {x : y for x, y in zip(l1, l2)}
print(d1)

print('--------------------------------------')

# Casting 형변환
print(float(3))
print(int(3.1))
print(str(4))
print(hex(12))
print(oct(10))
print(bin(10))

# list to tuple
print(tuple([1, 2]))

# tuple to list
print(list((3, 4)))

# list to 집합 데이터형
print(set([5, 6]))

# Two list to dictionary
print(dict([['a', 1], ['b', 2]]))  

# Unicode
print(ord('a'))
print(chr(97))

print('--------------------------------------')

# global and local
a = [1, 2, 3]
def temp():
    a = [4, 5, 6]
temp()
print(a)

def temp1():
    global a
    a = [4, 5, 7]
temp1()
print(a)

def templocal():
    a = 3
    print(locals())
templocal()

print('--------------------------------------')

