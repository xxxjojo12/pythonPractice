class Duck():
    def __init__(self, input_name):
        # __name 은 private
        self.__name = input_name

    @property
    def name(self):
        print('in getter')
        return self.__name

    @name.setter
    def name(self, input_name):
        print('in setter')
        self.__name = input_name


d1 = Duck('H')
d2 = Duck('A')

print(d1.name)
print(d2.name)

d1.name = 'd'

print(d1.name)
print(d1._Duck__name)5555