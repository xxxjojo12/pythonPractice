year, mon = map(int, input().split())

if year % 400 == 0 and mon == 2:
    print(29)

elif year % 4 == 0 and year % 100 != 0 and mon == 2:
    print(29)

elif mon == 1 or mon == 3 or mon == 5 or mon == 7 or mon == 8 or mon == 10 or mon == 12:
    print(31)
else:
    if mon == 2:
        print(28)
    else:
        print(30)