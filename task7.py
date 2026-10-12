class Patient:
    def __init__(self, pid, name, age, medicines):
        self.pid = pid
        self.name = name
        self.age = age
        self.medicines = medicines

patients = [
    Patient("P001", "Ali", 30, ["Paracetamol", "Amoxicillin"]),
    Patient("P002", "Sara", 25, ["Ibuprofen", "Antihistamine"]),
    Patient("P003", "Ahmed", 45, ["Metformin", "Atorvastatin"])
]

print("Patient Records:")
for p in patients:
    print(f"{p.pid}: {p.name}, Age {p.age}, Medicines: {p.medicines}")

# Deep copy of complete patient list
import copy
patient_list_copy = copy.deepcopy(patients)

# Modify medicine list of one patient in copied data
patient_list_copy[0].medicines = ["NewMedicine1", "NewMedicine2"]

print("\nAfter modifying copied data:")
print("Original patients[0] medicines:", patients[0].medicines)
print("Copied patients[0] medicines:", patient_list_copy[0].medicines)

print("\nOriginal data remains unchanged - deep copy works correctly")