class Animal:
    def __init__(self,name):
        self.name = name

    def speak(self):
        return "Sound of ," + self.name
    
class Dog(Animal):
    def speak(self):
        return "Woof! I am a dog named " + self.name
    


animal=Animal("Generic Animal")
animal_speak = animal.speak()
print(animal_speak)  # Output: Sound of ,Generic Animal
# Output: Sound of ,Generic Animal
 
# Create an instance of Dog
dog = Dog("Buddy")
# Call the speak method on the Dog instance
print(dog.speak())  # Output: Woof! I am a dog named Buddy


