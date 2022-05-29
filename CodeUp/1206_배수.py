a, b = map(int, input().split())

if a % b == 0 and a > b:
    n = a//b
    print(f'{b}*{n}={a}')
elif b % a == 0 and b > a:
    n = b//a
    print(f'{a}*{n}={b}')
elif a == b:
    print(f'{a}*{1}={b}')
else:
    print("none")