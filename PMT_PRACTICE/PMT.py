class HotelApp:
    def __init__(self):
        self.employees = []

    def get_employees(self):
        return self.employees

    def add_employee(self, employee):
        self.employees.append(employee)

    def get_monthly_employee_wages(self):
        amt = 0
        for employee in self.employees:
            amt += employee.get_monthly_wage()
        return amt


class Employee:
    def __init__(self, name):
        self.name = name
        self.salary = 0
        self.medical = 0
        self.wardrobe = 0
        self.education = 0
        self.annual_bonus = 0

    def get_name(self):
        return self.name

    def get_monthly_wage(self):
        return self.salary + self.medical + self.wardrobe + self.education + \
               self.annual_bonus/12


class Manager(Employee):
    def __init__(self, name):
        super().__init__(name)
        self.salary = 6000
        self.medical = 1000
        self.wardrobe = 500
        self.education = 1000
        self.annual_bonus = 3600


class Supervisor(Employee):
    def __init__(self, name):
        super().__init__(name)
        self.salary = 3000
        self.medical = 800
        self.wardrobe = 200
        self.education = 500
        self.annual_bonus = 2400


class EntryLevel(Employee):
    def __init__(self, name):
        super().__init__(name)
        self.salary = 1500
        self.medical = 500
        self.education = 400
        self.annual_bonus = 1200


def main():
    hotel = HotelApp()
    emp1 = Manager("John Smith")
    emp2 = Supervisor("Jane Jones")
    emp3 = EntryLevel("Ruth Sharp")

    hotel.add_employee(emp1)
    hotel.add_employee(emp2)
    hotel.add_employee(emp3)

    employees = hotel.get_employees()

    print("Employee List")
    print("=============\n")

    for i in range(len(employees)):
        print(f'{employees[i].get_name():<17}{"$"}'
              f'{employees[i].get_monthly_wage():>12,.2f}')
    print()
    print(f'{"Total wages: $"}'
          f'{hotel.get_monthly_employee_wages():>10,.2f}')

    emp4 = Manager("Dempsey Dean")
    emp5 = EntryLevel("Sophia Weather")

    hotel.add_employee(emp4)
    hotel.add_employee(emp5)

    print()

    for i in range(len(employees)):
        print(f'{employees[i].get_name():<17}{"$"}'
              f'{employees[i].get_monthly_wage():>12,.2f}')
    print()
    print(f'{"Total wages: $"}'
          f'{hotel.get_monthly_employee_wages():>10,.2f}')


main()
