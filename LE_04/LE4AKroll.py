# Name: Andrew Kroll
# Date: 2020-09-24
# Course-Section/LE#: CS1120-951 LE4
# Description: Employee, ProductionWorker, and ShiftManager data storage


class Employee:
    def __init__(self):
        self.employee_name = ""
        self.employee_number = 0

    def set_name(self, name: str):
        self.employee_name = name

    def get_name(self) -> str:
        return self.employee_name

    def set_number(self, number: int):
        self.employee_number = number

    def get_number(self) -> int:
        return self.employee_number


class ProductionWorker(Employee):
    def __init__(self):
        super().__init__()
        self.shift_number = 0
        self.hourly_pay = 0
        self.workday = 0

    def set_shift(self, shift: int):
        self.shift_number = shift

    def get_shift(self) -> int:
        return self.shift_number

    def set_hourly_pay(self, pay: float):
        self.hourly_pay = pay

    def get_hourly_pay(self) -> float:
        return self.hourly_pay

    def set_workday(self, workday: int):
        self.workday = workday

    def get_workday(self) -> int:
        return self.workday


class ShiftSupervisor(Employee):
    def __init__(self):
        super().__init__()
        self.salary = 0
        self.yearly_bonus = 0

    def set_salary(self, salary: float):
        self.salary = salary

    def get_salary(self) -> float:
        return self.salary

    def set_yearly_bonus(self, bonus: float):
        self.yearly_bonus = bonus

    def get_yearly_bonus(self) -> float:
        return self.yearly_bonus


def main():
    # Define worker object
    worker = ProductionWorker()
    # Set information
    print("Information for Production Worker:")
    worker.set_name(input("Name: "))
    worker.set_number(int(input("Employee Number: ")))
    worker.set_hourly_pay(float(input("Hourly Pay: $")))
    worker.set_shift(int(input("Shift Number: ")))
    worker.set_workday(int(input("Workday (Day = 1, Night = 2): ")))

    # Display information
    print()
    print("Production Worker's New Information:\n"
          "Name: {}\n"
          "Employee Number: {}\n"
          "Hourly Pay: ${}\n"
          "Shift Number: {}\n"
          "Workday: {}"
          .format(worker.get_name(), worker.get_number(),
                  worker.get_hourly_pay(), worker.get_shift(),
                  worker.get_workday()))


main()
