class word():
    def __init__(self, text):
        self.text = text

    def __eq__(self, word1):
        return self.text.lower() == word1.text.lower()

first = word('aaaa')
second = word('AaaAa')
third = word('asdafa')

print(first == second)
print(first == third)

