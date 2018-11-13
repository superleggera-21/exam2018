class Employee:
    """
    the base class
    """
    idnumber = 0
    def __init__(self, name):
        self.name = name
        self.id = (idnumber+1)
        idnumber += 1

    def get_name(self):
        return self.name

    def weekly_pay(self, hours_worked):
        return 0


class Nonexempt_Employee(Employee):

    def __init__(self, name, hourly_rate):
        Employee.__init__(self, name)
        self.hourly_rate = hourly_rate

    # Overrides the superclass method.
    def weekly_pay(self, hours_worked):
        if hours_worked > 40:
            return 40*self.hourly_rate + (hours_worked-40)*1.5*self.hourly_rate
        else:
            return hours_worked * self.hourly_rate

class Exempt_Employee(Employee):
    def __init__(self, name, annual_salary):
        Employee.__init__(self, name)
        self.hourly_rate = hourly_rate


class Manager(Exempt_Employee):
    pass  # delete this line and replace with your code here


def main():
    all_employees = []
    all_employees.append(Nonexempt_Employee("Aaron Wendell", 40.0))
    all_employees.append(Exempt_Employee("Alden Pexton", 60000.0))
    all_employees.append(Manager("Allison Fernandez", 94000.0, 50.0))

    for employee in all_employees:
        hours = int(input("Hours worked by " + employee.get_name() + ": "))
        pay = employee.weekly_pay(hours)
        print("Salary: ", pay)


if __name__ == '__main__':
    main()
