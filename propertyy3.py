class A():
    count = 0

    def __init__(self):
        A.count += 1

    def check(self):
        print("A class")

    @classmethod
    def tot(cls):
        print("Class A has", cls.count, "objects")


class B():
    @staticmethod
    def check():
        print("B class")


a = A()
b = A()
c = A()
d = A()

e = B()

print(a.check())
print(B.check())
print(e.check())

print(A.tot())
