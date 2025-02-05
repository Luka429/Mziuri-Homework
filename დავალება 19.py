class Animal:
    def __init__(self,name,color):
        self.name = name
        self.color = color

    def say_hi(self):
        print(F"Hello my name is {self.name} with color {self.color} and i am an animal")

class Dog(Animal):
    def say_hi(self):
        print(f"Hello my name is {self.name} with color {self.color} and i am a Dog")

dog1 = Dog("givi","black")
print(dog1.say_hi())
