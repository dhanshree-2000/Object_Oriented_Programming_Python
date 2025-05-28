from abc import ABC, abstractmethod
class MyABC(ABC):
    @abstractmethod
    def abstract_method1(self):
        """Method that must be implemented in subclass."""
        pass
    @abstractmethod
    def abstract_method2(self):
        """Another method that must be implemented in subclass."""
        pass
class ConcreteClass(MyABC):
    def abstract_method1(self):
        return "Implementation of abstract_method1"
    def abstract_method2(self):
        return "Implementation of abstract_method2"

# Creating an object of ConcreteClass
concrete = ConcreteClass()

# Calling the implemented methods
print(concrete.abstract_method1())  # Output: Implementation of abstract_method1
print(concrete.abstract_method2())  # Output: Implementation of abstract_method2