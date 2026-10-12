class Employee:
    def __init__(self, basic_salary=0, bonus_percent=0):
        self.__basic_salary = basic_salary
        self.__bonus_percent = bonus_percent

    @property
    def basic_salary(self):
        return self.__basic_salary

    @basic_salary.setter
    def basic_salary(self, value):
        if value >= 0:
            self.__basic_salary = value
        else:
            print(f"Error: basic_salary {value} must be non-negative.")

    @property
    def bonus_percent(self):
        return self.__bonus_percent

    @bonus_percent.setter
    def bonus_percent(self, value):
        if 0 <= value <= 50:
            self.__bonus_percent = value
        else:
            print(f"Error: bonus_percent {value} must be between 0% and 50%.")

    def gross_salary(self):
        return self.__basic_salary + (self.__basic_salary * self.__bonus_percent / 100)

    def raise_salary(self, percent):
        if percent > 30:
            print(f"Error: Salary increase of {percent}% rejected. Maximum allowed is 30%.")
        else:
            self.__basic_salary = self.__basic_salary * (1 + percent / 100)
            print(f"Salary increased by {percent}%. New basic salary: {self.__basic_salary:.2f}")


# Test all validation rules
emp = Employee(50000, 10)
print(f"Initial: salary={emp.basic_salary}, bonus={emp.bonus_percent}%, gross={emp.gross_salary()}")

emp.bonus_percent = 20
print(f"After setting bonus to 20%: gross={emp.gross_salary()}")

emp.bonus_percent = 60  # Invalid
print(f"After invalid bonus: gross={emp.gross_salary()}")

emp.basic_salary = 60000
print(f"After setting salary to 60000: gross={emp.gross_salary()}")

emp.basic_salary = -1000  # Invalid
print(f"After invalid salary: gross={emp.gross_salary()}")

emp.raise_salary(15)  # Valid
print(f"After 15% raise: gross={emp.gross_salary()}")

emp.raise_salary(50)  # Invalid (>30)
print(f"After rejected 50% raise: gross={emp.gross_salary()}")

emp.raise_salary(30)  # Valid (exactly 30)
print(f"After 30% raise: gross={emp.gross_salary()}")