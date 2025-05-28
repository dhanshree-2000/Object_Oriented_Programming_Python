class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        return f"{self.name} is eating."
    
class Mammal(Animal):
    def __init__(self, name, fur_color):
        super().__init__(name)
        self.fur_color = fur_color

    def walk(self):
        return f"{self.name} is walking on four legs which has {self.fur_color}."
    
class Dog(Mammal):
    def __init__(self, name, fur_color, breed):
        super().__init__(name, fur_color)
        self.breed = breed

    def bark(self):
        return f"{self.name} is barking which has {self.breed} breed."
    
# Create an instance of Dog
dog = Dog("Buddy", "Brown", "Golden Retriever")

dog_eat = dog.eat()  # Inherited from Animal
dog_walk = dog.walk()  # Inherited from Mammal
dog_bark = dog.bark()  # Defined in Dog
print(dog_eat)  # Output: Buddy is eating.
print(dog_walk)  # Output: Buddy is walking on four legs.
print(dog_bark)  # Output: Buddy is barking.