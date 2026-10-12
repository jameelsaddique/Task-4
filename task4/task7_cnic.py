class CNIC:
    def __init__(self, cnic_number):
        self.__cnic = cnic_number

    @property
    def number(self):
        return self.__cnic

    @property
    def masked(self):
        # Extract last four digits from CNIC format: 35202-1234567-1
        # The last four digits come from the middle segment
        parts = self.__cnic.split("-")
        if len(parts) >= 2 and len(parts[1]) >= 4:
            last_four = parts[1][-4:]
            return "*" * (len(self.__cnic) - 4) + last_four
        else:
            # fallback: just mask all but last 4
            return "*" * (len(self.__cnic) - 4) + self.__cnic[-4:]


# Test CNIC class
c = CNIC("35202-1234567-1")
print(f"Original: {c.number}")
print(f"Masked: {c.masked}")

# Demonstrate that setting number raises AttributeError
try:
    c.number = "35202-9876543-2"
    print("Setting number succeeded (unexpected)")
except AttributeError as e:
    print(f"Setting number raised AttributeError: {e}")