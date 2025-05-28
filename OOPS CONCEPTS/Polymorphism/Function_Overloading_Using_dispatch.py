from multipledispatch import dispatch
class Calculator:
    @dispatch(int, int)
    def add(self, a, b):
        return a + b


    @dispatch(float, float)
    def add(self, a, b):
        return a + b


    @dispatch(str, str)
    def add(self, a, b):
        return a + " " + b  # Concatenation for strings
# Creating an instance of Calculator
calc = Calculator()
# Calling overloaded methods
print(calc.add(5, 3))        # Output: 8
print(calc.add(2.5, 3.5))    # Output: 6.0
print(calc.add("Hello", "World"))  # Output: "Hello World"