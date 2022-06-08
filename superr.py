class Person():
    def __init__(self, name):
        self.name = name


class Student(Person):
    def __init__(self, name, grade):
        super().__init__(name)
        self.grade = grade


a = Person('A')
b = Student('B', 'freshman')

print(a.name)

print(b.name)
print(b.grade)
