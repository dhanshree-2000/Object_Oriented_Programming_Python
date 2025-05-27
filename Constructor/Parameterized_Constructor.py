class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Creating an object of the class with parameters
s1 = Student("John Doe", 20)
# Calling the method to display the name and age
s1.display()  # Output: Name: John Doe, Age: 20
