class Animal:
    def make_sound(self):
        print("Some sound")


class Dog(Animal):
    # Override make_sound to print "Bark"
    def make_sound(self):
        print("Some sound-Dog")


p = Dog()
p.make_sound()


# Create a Dog object and call make_sound()
