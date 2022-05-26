add = 0
for i in range(1, 1000):
    for j in range(2, 1000):
        if i%j == 0:
            break

    if i==j:
        add += i

print(add)

# Write a program that prints the sum of the prime numbers greater 
# than 2 and less than 1000