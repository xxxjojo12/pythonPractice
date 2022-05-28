a, b, c = map(int, input().split())

i = str(a)
j = str(b)
k = str(c)

if 0 < b < 10:
    j = "0"+ str(+b)

    if 0 <= c < 10:
        k = "00"+str(c)
    elif 9 < c < 100:
        k = "0"+str(c)

elif 9 < b < 100:

    if 0 <= c < 10:
        k = "00"+str(c)
    elif 9 < c < 100:
        k = "0"+str(c)

print(i+j+k)