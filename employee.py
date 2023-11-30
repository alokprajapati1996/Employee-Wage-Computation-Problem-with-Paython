"""

@Author: Alok kumar

@Date: 29-11-23 2:43:30

@Last Modified by: Alok kumar

@Last Modified time: 24-11-2023 4:00:30

@Title : Implementation of Employee Wage computation problem

"""
import random

print("welcome to Employee wage computation program")


def check_attandance():
    FULL_TIME = 1
    emp_type = random.randint(0, 1)
    if emp_type == FULL_TIME:
        print("Employee is Present")
    else:
        print("Employee is Absent")


if __name__ == '__main__':
    check_attandance()
