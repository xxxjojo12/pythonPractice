a, b, c = map(int, input().split())

n = (a-b+c)%10

if n == 0:
    print("대박")
elif n != 0:
    print("그럭저럭")