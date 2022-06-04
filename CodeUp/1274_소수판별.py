n = int(input())

for i in range(2, n):
    if n % i == 0 and n != 2:
        print("not prime")
        break
        
else:
    print("prime")
    