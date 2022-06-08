class vehicle():
    def check(self):
        print("this is a vehicle")

class car(vehicle):
    def check(self):
        print("This si a carrrr")

vehicle1 = vehicle()
car1 = car()
vehicle1.check()
car1.check()