a, b, c = map(int, input().split())

max_num = max(a, b, c)

if max_num == a and a < b+c:
    print("yes")
elif max_num == b and b < a+c:
    print("yes")
elif max_num == c and c < a+b:
    print("yes")
else:
    print("no")