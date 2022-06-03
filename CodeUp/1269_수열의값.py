a, b, c, d = map(int, input().split())

num = a

for i in range(d-1):
    num = num * b + c

print(num)
