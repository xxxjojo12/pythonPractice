a, b = map(int, input().split())

lt = []

for i in range(1, max(a, b)+1):
    lt.append(i)
    lt.append(i*10)

print(lt[a-1]+lt[b-1])