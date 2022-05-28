# a, b, c = map(int, input().split())

# if a > b and b > c:
#     print(b)
# elif a > c and c > b:
#     print(c)
# elif b > a and a > c:
#     print(a)
# elif b > c and c > a:
#     print(c)
# elif c > a and a > b:
#     print(a)
# elif c > b and b > a:
#     print(b)
# elif a > b and b == c:
#     print(b)
# elif b > a and a == c:
#     print(a)
# elif c > a and a == b:
#     print(a)
# else:
#     print(a)
nums = list(map(int, input().split()))

nums.sort()

print(nums[1])
