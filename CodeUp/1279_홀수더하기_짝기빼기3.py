a, b = map(int, input().split())

n = 0

for i in range(a, b+1):
    if i % 2 == 0:
        n -= i
        print(f'-{i}', end="")
    elif i % 2 != 0 and a != i:
        n += i
        print(f'+{i}', end="")
    else:
        n += i
        print(i, end = "")

print(f'={n}')