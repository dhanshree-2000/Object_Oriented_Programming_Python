class Animal:
    pass

class Dog(Animal):
    pass

class Cat(Animal):
    pass

print(issubclass(Dog, Animal))  # Output: True
print(issubclass(Cat, Animal))  # Output: True
print(issubclass(Dog, Cat))     # Output: False


print(isinstance(Dog(), Animal))  # Output: True
print(isinstance(Cat(), Animal))  # Output: True
print(isinstance(Dog(), Dog))     # Output: True
print(isinstance(Cat(), Dog))     # Output: False
print(isinstance(Dog(), Cat))     # Output: False
print(isinstance(Cat(), Cat))     # Output: True
