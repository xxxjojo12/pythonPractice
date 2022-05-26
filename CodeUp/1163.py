a, b, c = map(int, input().split())

n = ((a+b+c)/100)%10

if n%2 == 0:
    print("대박")
elif n%2 != 0:
    print("그럭저럭")