class StudentMarks:
    def __init__(self, marks=0):
        self.__marks = marks

    @property
    def marks(self):
        return self.__marks

    @marks.setter
    def marks(self, value):
        if 0 <= value <= 100:
            self.__marks = value
        else:
            print(f"Error: Marks {value} is invalid. Must be between 0 and 100. Previous value kept.")

    def grade(self):
        if self.__marks >= 90:
            return 'A'
        elif self.__marks >= 80:
            return 'B'
        elif self.__marks >= 70:
            return 'C'
        elif self.__marks >= 60:
            return 'D'
        else:
            return 'F'

    def __del__(self):
        print("StudentMarks object destroyed - cleanup message")


# Test with valid and invalid values
s = StudentMarks(85)
print(f"Initial marks: {s.marks}, Grade: {s.grade()}")

s.marks = 95
print(f"After setting to 95: {s.marks}, Grade: {s.grade()}")

s.marks = 150  # Invalid
print(f"After invalid set: {s.marks}, Grade: {s.grade()}")

s.marks = -10  # Invalid
print(f"After invalid set: {s.marks}, Grade: {s.grade()}")

s.marks = 75
print(f"After setting to 75: {s.marks}, Grade: {s.grade()}")

# Explicitly delete the object
del s
print("Object deleted - destructor should have printed above")