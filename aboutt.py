class A():
    def __init__(self, des):
        self.des = des


class B():
    def __init__(self, des):
        self.des = des


class C():
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def about(self):
        print(a.des, "  ", b.des)

a = A('aaaaaaa')
b = B('bbbbbbb')
c = C(a, b)

print(c.about())
