class Quote():
    def __init__(self, person, words):
        self.person = person
        self.words = words

    def who(self):
        return self.person

    def says(self):
        return self.words + '.'


class QuestionQuote(Quote):
    def says(self):
        return self.words + '?'


class ExclamationQuote(Quote):
    def says(self):
        return self.words + '!'


a = Quote('A', "AAAAAA")
print(a.who(), a.says())

a1 = QuestionQuote('A1', 'A111')
print(a1.who(), a1.says())

a2 = ExclamationQuote('A2', 'A222')
print(a2.who(), a2.says())
