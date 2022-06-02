n = int(input())
nums = list(map(int, input().split()))
b = 0
for i in range(n):
    if nums[i] % 5 == 0:
        b += nums[i]

print(b)