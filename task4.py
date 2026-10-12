class Employee:
    def __init__(self, emp_id, name, department, salary):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.salary = salary

employees = {
    "EMP001": Employee("EMP001", "Ali", "IT", 60000),
    "EMP002": Employee("EMP002", "Sara", "HR", 55000),
    "EMP003": Employee("EMP003", "Ahmed", "Finance", 70000)
}

print("Employee Directory:")
eid = "EMP001"  # Default employee ID to display
if eid in employees:
    emp = employees[eid]
    print(f"ID: {emp.emp_id}")
    print(f"Name: {emp.name}")
    print(f"Department: {emp.department}")
    print(f"Salary: {emp.salary}")
else:
    print("Employee not found")