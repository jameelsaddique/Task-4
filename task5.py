student = {
    "name": "Ali",
    "marks": [80, 75, 90],
    "subjects": ["Python", "OOP", "Database"]
}

import copy

# 1. Shallow copy
shallow = student.copy()

# 2. Deep copy
deep = copy.deepcopy(student)

print("Original student:", student)

# Modify marks in shallow copy
shallow["marks"][0] = 100
print("\nAfter modifying shallow copy marks[0] to 100:")
print("Original student marks:", student["marks"])
print("Shallow copy marks:", shallow["marks"])

# Reset original
student["marks"] = [80, 75, 90]

# Modify marks in deep copy
deep["marks"][1] = 99
print("\nAfter modifying deep copy marks[1] to 99:")
print("Original student marks:", student["marks"])
print("Deep copy marks:", deep["marks"])

print("\nShallow copy modifies original (marks list is shared)")
print("Deep copy does NOT modify original (independent copy)")