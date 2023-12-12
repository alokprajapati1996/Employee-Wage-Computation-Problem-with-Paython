"""

@Author: Alok kumar

@Date: 7-12-23 2:38:30

@Last Modified by: Alok kumar

@Last Modified time: 7-12-2023 3:30:30

@Title : Implementation of Employee Wage computation problem

"""
import random


class Employee:

    def __init__(self, emp_name, workings_hours, wage_per_hour, max_working_days, max_working_hours):
        self.emp_name = emp_name
        self.workings_hours = workings_hours
        self.wage_per_hour = wage_per_hour
        self.max_working_days = max_working_days
        self.max_working_hours = max_working_hours
        self.total_wage = 0

    def daily_emp_wage(self):
        """
         Description : This method to calculate employee salary
         parameter : None
         return : None

        """

        print("welcome to Employee wage computation")

        total_emp_hour = 0
        total_work_day = 0
        while total_emp_hour <= self.max_working_hours and total_work_day < self.max_working_days:
            emp_type = (random.randint(0, 2))
            match emp_type:
                case 0:
                    #  print(" Employee is Absent .")
                    self.workings_hours = 0
                case 1:
                    # print(" Employee is working full time .")
                    self.workings_hours = 8

                case 2:
                    # print(" Employee is working part-time.")
                    self.workings_hours = 4

            total_emp_hour += self.workings_hours
        self.total_wage = total_emp_hour * self.wage_per_hour
        print(f"{self.emp_name} One month total Employee wage : ", self.total_wage)


class Company:

    def __init__(self, comp_name):

        self.comp_name = comp_name
        self.employee_dict = {}

    def add_employee(self, emp_obj):
        self.employee_dict.update({emp_obj.emp_name: emp_obj})

    def get_employee(self, emp_name):
        emp_obj: Employee = self.employee_dict.get(emp_name)
        if emp_obj:

            print(f"Employee name : {emp_obj.emp_name} Total wage : {emp_obj.total_wage}")
        else:
            print("employee is not found.")

    def update_employee(self, emp_name):
        emp_obj: Employee = self.employee_dict.get(emp_name)
        if emp_obj:
            emp_obj.daily_emp_wage()
            self.employee_dict.update({emp_name: emp_obj})
        else:
            print("Employee is not Found!!")

    def delete_employee(self, emp_name):
        emp_obj: Employee = self.employee_dict.get(emp_name)
        if emp_obj:
            self.employee_dict.pop(emp_name)
        else:
            print("Employee is not Found!!")

    def display_employee(self):
        for key, value in self.employee_dict.items():
            print(f"Name : {key} | Total wage : {value.total_wage}  | Company :{self.comp_name}  ")


class MultipleCompany:

    def __init__(self):
        self.company_dict = {}

    def add_company(self, company_obj):
        self.company_dict.update({company_obj.comp_name: company_obj})

    def del_company(self, comp_name):
        multi_obj: MultipleCompany = self.company_dict.get(comp_name)
        if multi_obj:
            self.company_dict.pop(comp_name)
        else:
            print("Company is not Found!!")

    def get_company(self, comp_name):
        return self.company_dict.get(comp_name)

    def display_all_details(self):
        for key, value in self.company_dict.items():
            print(f"company: {key} | Total employee in Company : {len(value.employee_dict)}  ")


def main():
    multi_obj = MultipleCompany()
    while True:
        print("1.add a new employee in your emp wage")
        print("2.get a  employee in your  emp wage")
        print("3.update employee in your  emp wage")
        print("4.delete employee in your  emp wage")
        print("5.Display all employee details of employee wage")
        print("6.get company in your  emp wage")
        print("7.Display all company details of employee wage")
        print("8.delete  company in your  emp wage")
        print("9.for exit :")

        choice = int(input("enter your choice: "))

        match choice:
            case 1:

                comp_name = input("Enter company name :")

                if multi_obj.get_company(comp_name) is None:
                    company_obj = Company(comp_name)

                emp_name = input("Enter Employee name : ")
                workings_hours = int(input("enter working hours: "))
                wage_per_hour = int(input("enter working wage per hours: "))
                max_working_days = int(input("enter working days: "))
                max_working_hours = int(input("enter max working hours: "))
                emp_obj = Employee(emp_name, workings_hours, wage_per_hour, max_working_days, max_working_hours)
                emp_obj.daily_emp_wage()
                company_obj.add_employee(emp_obj)
                multi_obj.add_company(company_obj)
            case 2:
                comp_name = input("Enter company name: ")
                company_obj = multi_obj.get_company(comp_name)
                if company_obj:
                    emp_name = input("Enter employee name: ")
                    company_obj.get_employee(emp_name)

            case 3:
                comp_name = input("Enter company name: ")
                company_obj = multi_obj.get_company(comp_name)
                if company_obj:
                    emp_name = input("Enter employee name for update :")
                    company_obj.update_employee(emp_name)
            case 4:
                comp_name = input("Enter company name for update :")
                company_obj = multi_obj.get_company(comp_name)
                if company_obj:
                    emp_name = input("enter employee name you want to delete :")
                    company_obj.delete_employee(emp_name)
            case 5:
                comp_name = input("Enter the company name :")
                company_obj = multi_obj.get_company(comp_name)
                if company_obj:
                    company_obj.display_employee()
                else:
                    print("company not found.")
            case 6:
                comp_name = input("Enter company name: ")
                company_obj = multi_obj.get_company(comp_name)
                if company_obj:
                    print("company found")
                    print(f"company  {company_obj.comp_name}  total employee in : {len(company_obj.employee_dict)} ")
                    company_obj.display_employee()
                else:
                    print("company is not found")

            case 7:
                multi_obj.display_all_details()

            case 8:
                comp_name = input("enter company name you want to delete :")
                # company_obj = multi_obj.get_company(comp_name)
                # if company_obj:
                multi_obj.del_company(comp_name)
            case 9:
                break


if __name__ == '__main__':
    main()
