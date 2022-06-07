# n = int(input())

# m = n

# for i in range(2, n+1):
#     if m % i == 0 and n != i:
#         j = n//i
#         b = i
#         for a in range(2, j+1):
#             if j % a == 0 and a != j:
#                 print("wrong number")
#                 break
#             else:
#                 print(b, j)
#                 break
#         break
#     elif n == 1 or n == i:
#         print("wrong number")

# if n == 1:
#     print("wrong number")

a = int(input())
b = []

for i in range(2, a):
    if a % i == 0:
        b.append(i)

if len(b) == 2:
    if 4 in b:
        print("wrong number")
    else:
        print(*b)
else:
    print("wrong number")