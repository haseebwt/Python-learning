# Taken from inheritance practice lecture.

# Instances:
from ImportChildClass import Programmer

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