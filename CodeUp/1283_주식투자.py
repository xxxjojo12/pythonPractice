a = int(input())
b = int(input())
c = list(map(int, input().split()))

d = a

for i in c:
    d = d + (d * i/100)

e = round(d - a)

if e >= 1:
    print(f'{e}\ngood')
elif e <= -1:
    print(f'{e}\nbad')
else:
    print(f'{e}\nsame')