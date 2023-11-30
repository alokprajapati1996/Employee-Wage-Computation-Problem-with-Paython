"""

@Author: Alok kumar

@Date: 30-11-23 5:38:30

@Last Modified by: Alok kumar

@Last Modified time: 30-11-2023 10:30:30

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
PART_TIME = 2
WAGE_PER_HOUR = 20
emp_type = (random.randint(0, 2))
workings_hours = 0
if emp_type == FULL_TIME:
    print(" Employee is working full time")
    workings_hours = 8
elif emp_type == PART_TIME:
    print(" Employee is working part time.")
    workings_hours = 4
else:
    print(" Employee is Absent.")
emp_wage = workings_hours * WAGE_PER_HOUR
print("Employee daily wage is : ", emp_wage)

if __name__ == '__main__':
    daily_emp_wage()
