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

    # FULL_TIME = 1
    # PART_TIME = 2
    WAGE_PER_HOUR = 20
    NUM_OF_WORKING_DAYS = 20
    total_emp_wage = 0
    workings_hours = 0
    for day in range(0, NUM_OF_WORKING_DAYS):
        emp_type = (random.randint(0, 2))
        match emp_type:
            case 0:
                print(" Employee is Absent.", day)
                workings_hours = 0
            case 1:
                print(" Employee is working full time")
                workings_hours = 8
            case 2:
                print(" Employee is working part time.")
                workings_hours = 4
        emp_wage = workings_hours * WAGE_PER_HOUR
        total_emp_wage = total_emp_wage + emp_wage
    print("Employee daily wage is : ", total_emp_wage)


if __name__ == '__main__':
    daily_emp_wage()
