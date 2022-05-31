a, b, c = map(int, input().split())

n = 90 - a

if n > 0:
    if n % 5 == 0:
        i = n//5 + b
    else:
        i = n//5 + b + 1
else:
    i = b

if i > c:
    print("win")
elif i < c:
    print("lose")
elif i == c:
    print("same")