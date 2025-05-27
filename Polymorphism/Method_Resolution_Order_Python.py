class A:
    def __init__(self):
        print("A's constructor called")

    def method(self):
        print("Method from class A")

    def __del__(self):
        print("Destructor of A called")

class B(A):
    def __init__(self):
        super().__init__()  # Call A's constructor
        print("B's constructor called")

    def method(self):
        print("Method from class B")

    def __del__(self):
        print("Destructor of B called")
        super().__del__()

class C(A):
    def __init__(self):
        super().__init__()  # Call A's constructor
        print("C's constructor called")

    def method(self):
        print("Method from class C")

    def __del__(self):
        print("Destructor of C called")
        super().__del__()

class D(C, B):
    def __init__(self):
        super().__init__()  # Call B's constructor, which calls A's constructor
        print("D's constructor called")

    def method(self):
        print("Method from class D")

    def __del__(self):
        print("Destructor of D called")
        super().__del__()
    
# Example usage
d= D()
d.method()  # This will call D's method due to method resolution order (MRO)
print(D.mro())