n = int(input('Enter int: '))
root = 0
pwr = 0
for i in range(1, 100000):
    for j in range(2, 7):
        if n == i**j:
            root = i
            pwr = j
            break
if pwr == 0:
    print('x')
else:
    print(root, pwr)

# Write a program that asks the user to enter an integer
#  and prints two integers, root and pwr,
# such that 1 < pwr < 6 and root**pwr is equal to the integer
# entered by user. If no such pair of
# integers exists, is should print a message to that effect.