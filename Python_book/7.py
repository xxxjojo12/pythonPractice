n = int(input('Enter an integer: '))
i = 0

for pwr in range(1, 6):
    i += 1
    if i**pwr == n:
        print(i, pwr)
        exit()

if i <= n:
    print('No such pair of int exists')