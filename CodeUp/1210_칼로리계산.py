a, b = map(int, input().split())

dict = {1:400, 2:340, 3:170, 4:100, 5:70}

if dict[a]+dict[b] > 500:
    print("angry")
else:
    print("no angry")