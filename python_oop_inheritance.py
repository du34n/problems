
class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am  {self.name} and I am {self.age} years old")

class Cat(Pet):
    
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print("Meow")
    
class Dog(Pet):
    def speak(self):
        print("Bark")
    
p = Pet("Tim", 18)
p.show()

c = Cat("Bill", 12, "yellow")

c.show()