class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Sound of ," + self.name
    
class Dog(Animal):
    def speak(self):
        return "Woof! I am a dog named " + self.name
    
class Cat(Animal):
    def speak(self):
        return "Meow! I am a cat named " + self.name
    
class Cow(Animal):
    def speak(self):
        return "Moo! I am a cow named " + self.name
    
animals = [Dog("Buddy"), Cat("Whiskers"), Cow("Bessie")]

for animal in animals:
    print(animal.speak())




