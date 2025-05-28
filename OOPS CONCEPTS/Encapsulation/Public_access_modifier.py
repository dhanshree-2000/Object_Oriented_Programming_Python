class Student:
    def __init__(self,name):
        self.name = name

    def get_name(self):
        return self.name

std= Student("john")
print("Name:", std.get_name())  # This will work
print(std.name)  # This will also work, as name is a public attribute
