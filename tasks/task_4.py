class EmployeeSalary:
    hourly_payment = 400
    def __init__(self, name, hours, rest_days, email):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email

    @classmethod
    def get_hours(cls, name, rest_days, email):
        hours = (7 - rest_days) * 8
        return cls(name, hours, rest_days, email)

    @classmethod
    def get_email(cls, name, hours, rest_days):
        email = f"{name}@email.com"
        return cls(name, hours, rest_days, email)
    
    @classmethod
    def set_hourly_payment(cls, new_hourly_payment):
        cls.hourly_payment = new_hourly_payment

    def salary(self):
        salary = self.hours * self.hourly_payment
        return salary

# down_check_results
# employee = EmployeeSalary('Вася', 5, 1, 'kzkz@kd.ru')
# employee_2 = EmployeeSalary.get_hours('Гриша', 1, 'kzkz@kd.ru')
# employee_3 = EmployeeSalary.get_email('Гриша', 15, 2)
# print(employee.salary())
# print(employee_2.salary())
# print(employee_3.salary())

# new_salary = EmployeeSalary.set_hourly_payment(800)
# print(employee.salary())
# print(employee_2.salary())
# print(employee_3.salary())