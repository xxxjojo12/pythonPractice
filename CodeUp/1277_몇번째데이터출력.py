n = int(input())
lt = list(map(int, input().split()))

m = int(n-1)/2
mm = int(m)

print(lt[0], lt[mm], lt[n-1])