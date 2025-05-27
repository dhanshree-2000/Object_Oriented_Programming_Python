class Animal:
    def __init__(self,name):
        self.name = name

    def speak(self):
        return "Sound of ," + self.name
    
class Dog(Animal):
    def speak(self):
        return "Woof! I am a dog named " + self.name
    
class Cat(Animal):
    def speak(self):
        return "Meow! I am a cat named " + self.name


animal=Animal("Generic Animal")
animal_speak = animal.speak()
print(animal_speak)  # Output: Sound of ,Generic Animal
# Output: Sound of ,Generic Animal
 
# Create instances of Dog and Cat
dog = Dog("Buddy")
cat = Cat("Whiskers")
# Call the speak method on each instance
print(dog.speak())  # Output: Woof! I am a dog named Buddy
print(cat.speak())  # Output: Meow! I am a cat named Whiskers
# This example demonstrates inheritance in Python, where Dog and Cat classes inherit from the Animal class.
# Each subclass overrides the speak method to provide its own implementation.
# The Animal class serves as a base class, while Dog and Cat are derived classes that extend its functionality.