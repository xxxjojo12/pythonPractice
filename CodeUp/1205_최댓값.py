a, b = map(float, input().split())

i = a + b
j = a - b
k = b - a
l = a * b
m = a / b
n = b / a
o = a ** b
p = b ** a

nums = [i, j, k, l, m, n, o, p]

max_val = max(nums)

print(f'{max_val:.6f}')