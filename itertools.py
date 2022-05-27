import itertools

for item in itertools.chain([1, 2], ['a', 'b']):        #엮기
    print(item)

# for item in itertools.cycle([1, 2]):                  #무한반복
#     print(item, end=' ')

def multiply(a, b):
    return a * b

for item in itertools.accumulate([1, 2, 3, 4, 5, 6], multiply):   #누적, 다음꺼 더하기, 조건 설정 가능
    print(item)