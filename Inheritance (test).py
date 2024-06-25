# Inhertiance - Test:

# Two classes:
# Parent class = Employee
# Child class = Programmer

class Employee():

    def __init__(self, years_of_experience, position_name, employee_name):

        self.years_of_experience = years_of_experience
        self.position_name = position_name
        self.employee_name = employee_name

    def calculate_salary(self):

        base_salary = 2500

        if self.years_of_experience <= 2:
            calculated_salary = base_salary + 1500
            print(f"The salary is: {calculated_salary}")
            
        elif self.years_of_experience <= 5:
            calculated_salary = base_salary + 2500
            print(f"The salary is: {calculated_salary}")

        elif self.years_of_experience > 5:
            calculated_salary = base_salary + 3500
            print(f"The salary is: {calculated_salary}")

        else:
            print('Enter a valid value!')

        return calculated_salary
    

    def candidate_for_bonus(self, calculated_salary):


        if 'front_end' in self.position_name:
            bonus = calculated_salary * 1.1
            print(f"The bonus is: {bonus}")

        elif self.years_of_experience > 2:
            bonus = calculated_salary * 1.2
            print(f"The bonus is: {bonus}")

        else:
            print("Enter a valid value!")

        
class Programmer(Employee):
    
    def __init__(self, years_of_experience, position_name, employee_name):

        self.years_of_experience = years_of_experience
        self.position_name = position_name
        self.employee_name = employee_name
        super().__init__(years_of_experience, position_name, employee_name)

    def employee_info(self):

        print(f"The name of the employee is {self.employee_name}. They exhibit {self.position_name} position.")

# Instances:
junior_python_programmer = Programmer(1, "front_end", "Joseph")

senior_devops = Programmer(6, "senior_devops", "Dan")

# Execution:

junior_python_programmer.employee_info()
salary = junior_python_programmer.calculate_salary()
junior_python_programmer.candidate_for_bonus(salary)

print('\n')

senior_devops.employee_info()
salary = senior_devops.calculate_salary()
senior_devops.candidate_for_bonus(salary)