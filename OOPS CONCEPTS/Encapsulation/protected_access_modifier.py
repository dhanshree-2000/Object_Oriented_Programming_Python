class Student:
    def __init__(self,name):
        self._name=name # Protected attribute

    def _get_name(self):
        return self._name # Protected method
    
class GraduateStudent(Student):
    def display(self):
        print("Name:", self._get_name())   # Public method to access protected method

std= GraduateStudent("john")
std.display()  # This will work
# std._get_name()  # This will work, but it's not recommended to access protected members directly
# std._name  # This will work, but it's not recommended to access protected members directly