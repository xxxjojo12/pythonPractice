a, b = map(int, input().split())


if a > b:
    c = b
    d = a
elif a < b:
    c = a
    d = b
else:
    c = a
    d = a

for i in range(c, d+1):
    
    print(i, end = " ")