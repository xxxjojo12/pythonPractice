x = int(input('Enter int greater than 2: '))
s_div = None
if x%2 == 0:
    s_civ = 2
else:
    for guess in range(3, x, 2):
        if x % guess == 0:
            s_div = guess
            break
if s_div != None:
    print('S divisor of', x, 'is', s_div)
else:
    print(x, 'is a prime number')
    