class Vehicle:
    def start(self):
        print("Vehicle started")


class Car(Vehicle):
    pass


# Create a Car object and call start()
p = Car()
p.start()
