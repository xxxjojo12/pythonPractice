# n = int(input())

# j = n
# m = 0
# cnt = 0

# for i in range(1, n+1):
#     if j == i**2:
#         m == i
#         break
#     elif j != i**2:
#         j -= 1
#         cnt += 1

# print(cnt, m)
n = int(input())

root_n = n**0.5

t = int(root_n)
n_square = t**2
k = n - n_square

print(k, t)