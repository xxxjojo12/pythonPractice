nums = list(map(int, input().split()))

nums.sort()
# nums.remove(',')
# res = str(nums)[1:-1]
# print(res)
print(nums.pop(0), nums.pop(0), nums.pop(0))