a, b, c, d = map(int, input().split())

ans = a+b+c+d

if ans == 1:
    print("도")
elif ans == 2:
    print("개")
elif ans == 3:
    print("걸")
elif ans == 4:
    print("윷")
else:
    print("모")