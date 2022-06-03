dictionary1 = {1:'a', 2:'b', 3:'c', 4:'d'}
print(dictionary1)
dictionary1[5] = 'e'
print(dictionary1)
dictionary1[5] = 'E'
print(dictionary1)

dictionary2 = {6:'f', 7:'g'}
print(dictionary1, dictionary2)
dictionary1.update(dictionary2)  #dic1에 dic2 추가
print(dictionary1, dictionary2)

dic3 = {6:'F'}
print(dictionary1, dictionary2, dic3)
dictionary1.update(dic3)
print(dictionary1, dictionary2, dic3)
print(dictionary1.update(dic3), dictionary2, dic3)
del dictionary1[6]    #부분 지우기
print(dictionary1)

print(1 in dictionary1)  #True '1'은 False
print(dictionary1[1])    #[]안에 있는거 뽑기
print(dictionary1.get(1)) #위랑 똑같음




print(dictionary1.keys()) #dictionary안에 키값들 다 뽑기
print(dictionary1.values())  #dictionary안에 밸류 다 뽑기

print(list(dictionary1.keys()))    #dictionary를 list로 바꾸기
print(list(dictionary1.values()))
print(list(dictionary1.items()))   #다 바꾸기

dic4 = dictionary1.copy()  #복사하기

dictionary1.clear()   #다 지우기
print(dictionary1, dic4)

