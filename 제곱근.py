epsilon = 0.01
x = int(input('Enter an number: '))

if x < 0:
    print('Does not exist')
else:
    low = 0
    high = max(1, x)
    ans = (high + low)/2
    while abs(ans**3 - x) >= epsilon:
        if ans**3 <x:
            low = ans
        else:
            high = ans
        ans = (high + low)/2
    print(ans, 'is close to square root of ', x)