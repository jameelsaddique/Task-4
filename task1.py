class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

students = [
    Student("Ali", "S1", 85),
    Student("Sara", "S2", 92),
    Student("Ahmed", "S3", 78),
    Student("Fatima", "S4", 95)
]

print("Name | Roll No | Marks")
print("-" * 30)
for s in students:
    print(f"{s.name:6} | {s.roll_no:8} | {s.marks}")

print("\n--- Update marks of one student through the list ---")
students[2].marks = 88
print(f"After updating students[2].marks to 88:")
print(f"Ahmed's marks: {students[2].marks}")