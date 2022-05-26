set1 = set()

seta = {1, 2, 3, 4, 5}
setb = {3, 4, 5}

print(set1, seta, setb)

print(seta & setb)   #같은게 있냐
print(seta.intersection(setb))  #위랑 같음

print(seta | setb)   #합집합
print(seta.union(setb))  #위랑 같음

print(seta - setb) #빼기
print(seta.difference(setb)) #위랑 같음

print(seta ^ setb) #합집합하고 교집합 빼기
print(seta.symmetric_difference(setb))  #위랑 같음

print(seta <= setb)  #seta가 setb의 부분집합인가
print(seta.issubset(setb))  #위랑 같음

print(seta >= setb)  #setb가 seta의 부분집합인가
print(setb.issubset(seta))  #위랑 같음
print(seta.issuperset(setb)) #위랑 같음

print(seta.isdisjoint(setb))  #intersection이 있냐, 있으면 false 없으면 true