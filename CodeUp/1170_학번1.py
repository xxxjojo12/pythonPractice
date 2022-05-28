a, b, c = map(int, input().split())

i = str(a)
j = str(b)
k = str(c)

if c < 10:
    print(i + j + "0" + k)
else:
    print(i + j + k)