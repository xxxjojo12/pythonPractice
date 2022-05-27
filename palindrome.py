from collections import deque

def palindrome(word):
    dq = deque(word)
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
    return True

def palindrome1(word):
    return word == word[::-1]

print(palindrome('A'))
print(palindrome('AacaA'))
print(palindrome('ABBCA'))
print(palindrome('ABCDE'))