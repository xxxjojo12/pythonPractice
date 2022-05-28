a, b = map(int, input().split())

n = a // 10000

if b == 1 or b == 2:
    print(113-n)
elif b == 3 or b == 4:
    print(2013-2000-n)