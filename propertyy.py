class Duck():
    def __init__(self, input_name):
        self.hidden_name = input_name

    @property
    def name(self):
        print('in getter')
        return self.hidden_name

    @name.setter
    def name(self, input_name):
        print('in setter')
        self.hidden_name = input_name

    # name = property(get_name, set_name)


duck1 = Duck('Hail')
print(duck1.name)

duck1.name = 'Sujin'
print(duck1.name)
