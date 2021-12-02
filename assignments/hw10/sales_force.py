"""
Name: Angela Nganga
sales_force.py
Problem: This program uses list methods and compares search/sort algorithms
Certification of Authenticity:
I certify that this assignment is entirely my own work, however I discussed it with tutors at the CSL.
"""
from sales_person import *


class SalesForce:

    def __init__(self):
        self.sales_people = []

    def add_data(self, file_name):
        in_file = open(file_name, 'r')
        lines = in_file.readlines()
        for i in range(len(lines)):
            data = lines[i].split(", ")
            person = SalesPerson(eval(data[0]), data[1])
            sales = data[2].split()
            for i in range(len(sales)):
                person.enter_sale(float(sales[i]))
            self.sales_people.append(person)

    def quota_report(self, quota):
        report = []
        for i in range(len(self.sales_people)):
            report.append(
                [self.sales_people[i].get_id(), self.sales_people[i].get_name(), self.sales_people[i].total_sales(),
                 self.sales_people[i].total_sales() > quota])
        return report

    def top_seller(self):
        top = self.sales_people[0]
        top_seller_list = []
        for i in range(len(self.sales_people)):
            if self.sales_people[i].compare_to(top) > 0:
                top = self.sales_people[i]
                top_seller_list = []
            elif self.sales_people[i].compare_to(top) == 0:
                top_seller_list.append(self.sales_people[i])
        top_seller_list.append(top)
        return top_seller_list

    def individual_sales(self, employee_id):
        for i in range(len(self.sales_people)):
            if self.sales_people[i].get_id() == employee_id:
                return self.sales_people[i]
        return None


def main():
    target = SalesForce()
    target.add_data("salesData.txt")
    print(target.quota_report(300))
    print(target.top_seller())
    print(target.individual_sales(123))

main()
