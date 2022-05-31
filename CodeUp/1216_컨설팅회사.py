a, b, c = map(int, input().split())

n = b - c

if a > n:
    print("do not advertise")
elif a < n:
    print("advertise")
else:
    print("does not matter")