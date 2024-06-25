# OOP - Object Creation and Implementation

# Example of class with multiple functions and a main function called "__init__"
# The __init__ function basically takes values from the user and stores them in the class to be used in an instance.

class Employee:

    def __init__(self, name, salary, attendance):
        self.name = name
        self.salary = salary
        self.attendance = attendance

    def employee_details(self):

        print("Employee name: "+self.name+ ". Emloyee salary: "+str(self.salary))

    def check_attendance(self):

        print(f"Employee name: {self.name}. Employee attendance: {self.attendance}")

        if self.attendance < 4:
            print(f"{self.name} has been kicked out from the facility for having a reduced attendance than their peers.")
        else:
            pass


emp1 = Employee('Haseeb', 20000, 6)
emp1.employee_details()
emp1.check_attendance()

print("\n")

emp2 = Employee('Rachel', 10000, 2)
emp2.employee_details()
emp2.check_attendance()