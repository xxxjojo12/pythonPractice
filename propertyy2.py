class Circle():
    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return 2 * self.radius

    @diameter.setter
    def diameter(self, diameter):
        self.radius = int(diameter / 2)


c = Circle(5)
print(c.radius)
print(c.diameter)

c.radius = 7
print(c.radius)
print(c.diameter)

c.diameter = 10
print(c.radius)
print(c.diameter)
