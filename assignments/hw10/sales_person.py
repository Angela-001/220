"""
Name: Angela Nganga
sales_person.py
Problem: This program uses an object with a list and uses a list of objects
Certification of Authenticity:
I certify that this assignment is entirely my own work, however I discussed it with tutors at the CSL.
"""


class SalesPerson:
    """
    Salesperson class containing employee_id, name and sales.
    """

    def __init__(self, employee_id, name):
        self.employee_id = employee_id
        self.name = name
        self.sales = []

    def get_id(self):
        return self.employee_id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def enter_sale(self, sale):
        self.sales.append(sale)

    def total_sales(self):
        total = 0
        for num in self.sales:
            total = total + float(num)
        return total

    def get_sales(self):
        return self.sales

    def met_quota(self, quota):
        if self.total_sales() >= quota:
            return True
        return False

    def compare_to(self, other):
        if other.total_sales() > self.total_sales():
            return -1
        elif self.total_sales() > other.total_sales():
            return 1
        return 0

    def __str__(self):
        return str(self.employee_id) + "-" + self.name + ": " + str(self.total_sales())

    def __repr__(self):
        return str(self.employee_id) + "-" + self.name + ": " + str(self.total_sales())

def main():
    person1 = SalesPerson(123, "John Smith")
    print(person1.get_id())
    print(person1.get_name())
    person1.set_name("Charles North")
    print(person1.get_name())
    sale = 50.0
    person1.enter_sale(sale)
    print(person1.total_sales())
    print(person1.get_sales())
    print(person1.met_quota(80.0))
    print(person1.met_quota(3.0))
    person2 = SalesPerson(234, "Albert Einstein")
    person2.enter_sale(100.0)
    person2.enter_sale(12.5)
    print(person2.get_sales())
    print(person2.total_sales())
    print(person1.compare_to(person2))
    print(person2.compare_to(person1))

main()
