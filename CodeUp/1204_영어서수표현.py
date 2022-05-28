n = int(input())

m = n%10

if 11<=n<=13:
    print(f'{n}th')
elif m == 1:
    print(f'{n}st')
elif m == 2:
    print(f'{n}nd')
elif m == 3:
    print(f'{n}rd')
else:
    print(f'{n}th')