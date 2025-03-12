class Animal:
    def __init__(self):
        self.eyes = 2

    def breathing(self):
        print("It inhale ")

class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breathing(self):
        super().breathing()
        print("It inhale under water")
    def swim(self):
        print("Swimming under the water")


fish = Fish()
fish.swim()
fish.breathing()
print(fish.eyes)
