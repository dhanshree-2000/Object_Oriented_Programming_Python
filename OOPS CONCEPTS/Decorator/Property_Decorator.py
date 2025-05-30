class Employee:
    def __init__(self,first,last):
        self.first = first
        self.last = last

    @property
    def fullname(self):
        return f'{self.first} {self.last}'
    
    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)
    
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None

emp1 = Employee('John', 'Doe')
emp1.first = 'Jane'  # This will not change the fullname or email properties
print(emp1.fullname)  # Output: John Doe
print(emp1.email)     # Output:

emp1.fullname = 'Dhanshree Kadam'  # This will raise an AttributeError
print(emp1.fullname)  # Output: John Doe
print(emp1.email)  