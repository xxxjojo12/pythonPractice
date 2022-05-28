n = int(input())

a = n//10
b = (n % 10)*10
c = (a + b)*2

if c <= 50:
    print(c)
    print("GOOD")
elif 50 < c < 100:
    print(c)
    print("OH MY GOD")
elif c >= 100:
    d = c % 100
    if d <= 50:
        print(d)
        print("GOOD")
    elif 50 < d < 100:
        print(d)
        print("OH MY GOD")
