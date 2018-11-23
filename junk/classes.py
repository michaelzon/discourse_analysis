# tutorial

class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@live.nl"

        Employee.num_of_emps += 1

    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

emp_1 = Employee("Michael", "Zonneveld", 4000)
emp_2 = Employee("Jan", "Vries", 2000)

# print(Employee.__dict__)

emp_1.raise_amount = 1.05

print(emp_1.__dict__)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

# onderstaande geeft dezelfde code
# print(emp_1.fullname())
# print(Employee.fullname(emp_1))


# class variabele = zelfde waarde over alle instanties
# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)

# emp_1.raise_amount
# Employee().raise_amount
