class Demart:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __lt__(self, other):
        return self.price < other.price

    def __le__(self, other):
        return self.price <= other.price

    def __eq__(self, other):
        return self.price == other.price

    def __ne__(self, other):
        return self.price != other.price

    def __gt__(self, other):
        return self.price > other.price

    def __ge__(self, other):
        return self.price >= other.price
    
    def __str__(self):
        return f"{self.name}: ${self.price:.2f}"
    
# Example usage
d1 = Demart("Item A", 10.99)
d2 = Demart("Item B", 15.49)
print(f"Comparing {d1} and {d2}:")
print(f"{d1} < {d2}: {d1 < d2}")
print(f"{d1} <= {d2}: {d1 <= d2}")
print(f"{d1} == {d2}: {d1 == d2}")
print(f"{d1} != {d2}: {d1 != d2}")
print(f"{d1} > {d2}: {d1 > d2}")
print(f"{d1} >= {d2}: {d1 >= d2}")
