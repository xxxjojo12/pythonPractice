a, b, c, d = map(int, input().split())

i = a/b
j = c/d

if i > j:
    print(">")

elif i < j:
    print("<")

elif i == j:
    print("=")