# Version 1: Public Attribute (no validation)
class TemperaturePublic:
    def __init__(self, celsius=0):
        self.celsius = celsius


# Version 2: Encapsulated Attribute with validation
class TemperatureEncapsulated:
    def __init__(self, celsius=0):
        self.__celsius = celsius

    @property
    def celsius(self):
        return self.__celsius

    @celsius.setter
    def celsius(self, value):
        if -273.15 <= value <= 1000:
            self.__celsius = value
        else:
            print(f"Error: {value} is out of range. Must be between -273.15 and 1000.")


# Test both versions with invalid assignments
print("=== Version 1: Public Attribute (no validation) ===")
t1 = TemperaturePublic()
t1.celsius = 50
print(f"Set to 50: {t1.celsius}")
t1.celsius = -300  # Invalid, no validation
print(f"Set to -300: {t1.celsius}")
t1.celsius = 2000  # Invalid, no validation
print(f"Set to 2000: {t1.celsius}")

print("\n=== Version 2: Encapsulated Attribute (with validation) ===")
t2 = TemperatureEncapsulated()
t2.celsius = 50
print(f"Set to 50: {t2.celsius}")
t2.celsius = -300  # Invalid, should be rejected
print(f"After invalid set: {t2.celsius}")
t2.celsius = 2000  # Invalid, should be rejected
print(f"After invalid set: {t2.celsius}")

print("\n=== Comparison ===")
print("When data is public and unvalidated, invalid values can be assigned directly")
print("without any checks, leading to potential bugs, corrupted state, and")
print("unpredictable behavior in calculations. Encapsulation with validation")
print("protects the data integrity and ensures only reasonable values are stored.")