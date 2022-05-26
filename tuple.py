empty_tuple = ()
empty_tuple = 'a', 'b', 'c'
print(empty_tuple)
a, b, c = empty_tuple
print(a, b, c)

list1 = ['sdfsdf', 'adfewrq','einwioen','owienr']
print(list1)
print(tuple(list1))  #tuple화 하는거

empty_dictionary = {}
dictionary1 = {'a':'This is A', 'b':'This is B', 'c':'This is C'}
print(dictionary1)

list2 = [[1, 'a'], [2, 'b'], [3, 'c']]
print(list2)
print(dict(list2))   #dictionary화 하는거

til = [('a', 1), ('b', 2), ('c', 3)]
print(til)
print(dict(til))  #list안에 tuple을 dictionary화

list3 = ['qw', 'we', 'df']
print(list3)
print(dict(list3))   #두자리 string이면 일케댐

