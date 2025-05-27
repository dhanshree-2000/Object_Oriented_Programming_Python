class student:
    def __init__(self,name):
        self.__name=name # Private attribute

    def __get_name(self):
        return self.__name # Private method
    
    def display(self):
        print("Name:", self.__get_name())   # Public method to access private method


std= student("john")
std.display()  # This will work

# std.__get_name()  # This will raise an AttributeError because __get_name is private
# std.__name  # This will raise an AttributeError because __name is private