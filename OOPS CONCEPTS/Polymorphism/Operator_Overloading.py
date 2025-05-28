class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        return Complex(self.real * other.real - self.imag * other.imag,
                       self.real * other.imag + self.imag * other.real)

    def __str__(self):
        return f"{self.real} + {self.imag}i"

# Example usage
c1 = Complex(2, 3)
c2 = Complex(4, 5)
c3 = c1 + c2
c4 = c1 - c2
c5 = c1 * c2
print(f"c1: {c1}")
print(f"c2: {c2}")
print(f"c1 + c2: {c3}")
print(f"c1 - c2: {c4}")
print(f"c1 * c2: {c5}")
