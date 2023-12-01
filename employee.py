"""

@Author: Alok kumar

@Date: 1-12-23 2:38:30

@Last Modified by: Alok kumar

@Last Modified time: 1-12-2023 3:30:30

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
    wage_per_hour = 20
    total_emp_wage = 0
    workings_hours = 0
    max_working_days = 20
    max_working_hours = 100
    total_emp_hour = 0
    total_work_day = 0
    while total_emp_hour <= max_working_hours and total_work_day < max_working_days:
        emp_type = (random.randint(0, 2))
        total_work_day = total_work_day + 1
        match emp_type:
            case 0:
                print(" Employee is Absent .")
                workings_hours = 0
            case 1:
                print(" Employee is working full time .")
                workings_hours = 8
            case 2:
                print(" Employee is working part time.")
                workings_hours = 4
        total_emp_hour += workings_hours
        total_emp_wage = total_emp_hour * wage_per_hour
    print("One month total Employee wage : ", total_emp_wage)


if __name__ == '__main__':
    daily_emp_wage()
