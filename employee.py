"""

@Author: Alok kumar

@Date: 1-12-23 2:38:30

@Last Modified by: Alok kumar

@Last Modified time: 1-12-2023 3:30:30

@Title : Implementation of Employee Wage computation problem

"""
import random


class Employee:

    def __init__(self, emp_name, workings_hours, max_working_days, max_working_hours):
        self.emp_name = emp_name
        self.workings_hours = workings_hours
        self.max_working_days = max_working_days
        self.max_working_hours = max_working_hours

    def daily_emp_wage(self):
        """
         Description : 
         parameter : None
         return : None

        """

        print("welcome to Employee wage computation")

        total_emp_wage = 0
        total_emp_hour = 0
        total_work_day = 0
        while total_emp_hour <= self.max_working_hours and total_work_day < self.max_working_days:
            emp_type = (random.randint(0, 2))
            total_work_day = total_work_day + 1
            match emp_type:
                case 0:
                    print(" Employee is Absent .")
                    self.workings_hours = 0
                case 1:
                    print(" Employee is working full time .")
                    self.workings_hours = 8
                case 2:
                    print(" Employee is working part time.")
                    self.workings_hours = 4
            total_emp_hour += self.workings_hours
            total_emp_wage = total_emp_hour * wage_per_hour
        print(f"{self.emp_name} One month total Employee wage : ", total_emp_wage)


def main():
    emp_name = input("Enter Employee name : ")
    workings_hours = int(input("enter working hours: "))
    max_working_days = int(input("enter working days: "))
    max_working_hours = int(input("enter max working hours: "))

    emp_obj = Employee(emp_name, workings_hours, max_working_days, max_working_hours)
    emp_obj.daily_emp_wage()


if __name__ == '__main__':
    main()
