a, b, c = map(int, input().split())

if a == b and b == c:
    print("정삼각형")
elif (a == b or b == c) and c < a+b:
    print("이등변삼각형")
elif (a**2)+(b**2) == c**2 or (b**2)+(c**2) == a**2 or (a**2)+(c**2) == b**2:
    print("직각삼각형")
elif c < a+b:
    print("삼각형")
else:
    print("삼각형아님")