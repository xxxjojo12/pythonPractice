print('I am thinking of a number between 1 and 20.')
ans = 16
n = 0

while 1:
    n += 1
    print('Take a guess.')
    num = int(input())
    if num < 16:
        print('Your guess is too low.')
        continue
    elif num > 16:
        print('Your guess is too high.')
        continue
    else:
        print(f'Good job! You guessed my number in {n} guesses!')
        break