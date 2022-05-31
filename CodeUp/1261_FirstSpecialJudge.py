from sys import stdin

ten_nums = list(map(int, stdin.readline().split()))

for num in ten_nums:
    if num % 5 == 0:
        print(num)
        break
else:
    print(0)