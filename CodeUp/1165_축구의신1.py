a, b = map(int, input().split())

n = 90 - a

if n > 0:
    if n % 5 == 0:
        print(n//5 + b)
    else:
        print(n//5 + b + 1)
else:
    print(b)