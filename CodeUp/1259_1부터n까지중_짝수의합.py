a = int(input())

cnt = 0

for i in range(1, a+1):
    if i % 2 == 0:
        cnt += i

print(cnt)