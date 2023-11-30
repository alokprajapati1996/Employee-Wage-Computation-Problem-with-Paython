"""

@Author: Alok kumar

@Date: 30-11-23 10:38:30

@Last Modified by: Alok kumar

@Last Modified time: 30-11-2023 4:11:30

@Title : Implementation of Employee Wage computation problem

"""
import random


def daily_emp_wage():
    """
    @parameter : None

    :return : None

    """

    print("welcome to Employee wage computation")

FULL_TIME = 1
WAGE_PER_HOUR = 20
emp_type = (random.randint(0, 1))
workings_hours = 0
if emp_type == FULL_TIME:

    print(" Employee is present.")
    workings_hours = 8
else:
    print(" Employee is Absent.")
wage = workings_hours * WAGE_PER_HOUR
print("Employee daily wage is : ", wage)

if __name__ == '__main__':
    daily_emp_wage()
