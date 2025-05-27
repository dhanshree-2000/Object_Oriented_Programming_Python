class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_name(self):
        return self.name
    
    def get_salary(self):
        return self.salary

    def display(self):
        print(f"Name: {self.name}, Salary: {self.salary}")

class Manager:
    def __init__(self, emp_id):
        self.emp_id = emp_id

    def get_employee_id(self):
        return self.emp_id

    def display(self):
        print(f"Employee ID: {self.emp_id}")

class Company(Employee, Manager):
    def __init__(self, name, salary, employee_id, department):
        self.department = department
        Employee.__init__(self, name, salary) #this initializes the Employee part of the class
        Manager.__init__(self, employee_id)

    def display(self):
        print(f"Name: {self.get_name()}, Salary: {self.get_salary()}, Empolyee_id:{self.get_employee_id() }, Department: {self.department}")
        Employee.display(self)
        Manager.display(self)


company_instance = Company("Alice", 80000, "EMP123", "Engineering")
company_instance.display()  # Output: Name: Alice, Salary: 80000, Department: Engineering