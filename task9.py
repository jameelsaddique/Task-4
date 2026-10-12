class Employee:
    def __init__(self, emp_id, name, team):
        self.emp_id = emp_id
        self.name = name
        self.team = team

employee1 = Employee("E1", "Ali", "Python Team")
employee2 = Employee("E2", "Sara", "Python Team")
employee3 = Employee("E3", "Ahmed", "Web Team")
employee4 = Employee("E4", "Fatima", "Web Team")

teams = {
    "Python Team": [employee1, employee2],
    "Web Team": [employee3, employee4]
}

print("Original Teams:")
for team, emps in teams.items():
    print(f"\n{team}:")
    for e in emps:
        print(f"  - {e.name} (ID: {e.emp_id})")

import copy
# Shallow copy of teams
teams_shallow = teams.copy()

# Deep copy of teams
teams_deep = copy.deepcopy(teams)

# Modify employee info in shallow copy
teams_shallow["Python Team"][0].name = "Ali Updated"

# Modify employee info in deep copy
teams_deep["Web Team"][1].name = "Fatima Updated"

print("\n\nShallow copy modification:")
print("Original Python Team[0] name:", employee1.name)
print("Shallow copy Python Team[0] name:", teams_shallow["Python Team"][0].name)
print("Original affected:", employee1.name != "Ali")

print("\nDeep copy modification:")
print("Original Web Team[1] name:", employee4.name)
print("Deep copy Web Team[1] name:", teams_deep["Web Team"][1].name)
print("Original affected:", employee4.name != "Fatima")

print("\nShallow copy: Original structure changes when copy is modified")
print("Deep copy: Original structure remains unchanged")