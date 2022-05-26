y = 0
for counter in range(10):
    x = int(input("Enter a number: "))
    if (x%2 == 1 and x > y):
        y = x

if (y == 0):
    print("All are even")
else:
   print(y, "is the largest odd number")