class Course:
    def __init__(self, name, code, credits):
        self.name = name
        self.code = code
        self.credits = credits

courses = (
    Course("Python Programming", "CS101", 3),
    Course("Data Structures", "CS102", 3),
    Course("Database Systems", "CS103", 3),
    Course("Web Development", "CS104", 3)
)

print("All Courses:")
print("-" * 40)
for i, c in enumerate(courses):
    print(f"{i}: {c.name} ({c.code}) - {c.credits} credits")

print(f"\nAccess course at index 2: {courses[2].name} ({courses[2].code})")