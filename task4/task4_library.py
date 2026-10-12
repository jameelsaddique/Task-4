class Library:
    def __init__(self):
        self.__borrowed = []

    def borrow_book(self, title):
        if title in self.__borrowed:
            print(f"Error: '{title}' is already borrowed.")
        else:
            self.__borrowed.append(title)
            print(f"'{title}' borrowed successfully.")

    def return_book(self, title):
        if title not in self.__borrowed:
            print(f"Error: '{title}' is not currently borrowed.")
        else:
            self.__borrowed.remove(title)
            print(f"'{title}' returned successfully.")

    def get_borrowed(self):
        return self.__borrowed.copy()


lib = Library()
lib.borrow_book("Python 101")
lib.borrow_book("Data Structures")

print("\nOriginal borrowed list via get_borrowed():", lib.get_borrowed())

# Modify the returned list
borrowed_copy = lib.get_borrowed()
borrowed_copy.append("New Book")
print("After appending to returned list:")

print("Returned list:", borrowed_copy)
print("Original private list via get_borrowed():", lib.get_borrowed())

print("\nDemonstration complete - original list unchanged.")