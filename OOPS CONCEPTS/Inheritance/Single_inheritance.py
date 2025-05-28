class Base:
    var1=10
    def __init__(self):
        print("Base class constructor called")

class Derived(Base):
    def __init__(self):
        print("Derived class constructor called")

    def show(self):
        print("Value of var1 from Base class:", self.var1)

class Derived2(Base):
    def show2(self):
        print("Value of var1 from Base class in Derived2:", Base.var1)

class Derived3(Base):
    def show3(self):
        print("Value of var1 from Base class in Derived3:", super().var1)



# Create an instance of the Derived class
derived_instance = Derived()
# Call the show method to access var1 from the Base class
derived_instance.show()  # Output: Value of var1 from Base class: 10
# This example demonstrates single inheritance in Python, where the Derived class inherits from the Base class.
# The Derived class can access attributes and methods of the Base class, allowing for code reuse and extension of functionality.

derived_instance2 = Derived2()
derived_instance2.show2()  # Output: Value of var1 from Base class in Derived2: 10


derived_instance3 = Derived3()
derived_instance3.show3()  # Output: Value of var1 from Base class in Derived3: 10