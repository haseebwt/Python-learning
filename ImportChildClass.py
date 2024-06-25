# Class taken from inheritance practice.


from ImportParentClass import Employee


class Programmer(Employee):
    
    def __init__(self, years_of_experience, position_name, employee_name):

        self.years_of_experience = years_of_experience
        self.position_name = position_name
        self.employee_name = employee_name
        super().__init__(years_of_experience, position_name, employee_name)

    def employee_info(self):

        print(f"The name of the employee is {self.employee_name}. They exhibit {self.position_name} position.")