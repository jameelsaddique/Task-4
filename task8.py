class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

product1 = Product("iPhone", 99999)
product2 = Product("Samsung", 79999)
product3 = Product("Dell Laptop", 129999)
product4 = Product("MacBook", 249999)

categories = {
    "Laptops": [product1, product2],
    "Mobiles": [product3, product4]
}

print("Original Category Structure:")
for cat, prods in categories.items():
    print(f"\n{cat}:")
    for p in prods:
        print(f"  - {p.name}: {p.price}")

import copy
# Deep copy of complete category structure
categories_copy = copy.deepcopy(categories)

# Modify one product's information in the copy
categories_copy["Laptops"][0].name = "iPhone 15"
categories_copy["Laptops"][0].price = 109999

print("\n\nAfter modifying copy:")
print("Original structure changes:", end=" ")
# Check if original changed
original_changed = (product1.name != "iPhone" or product1.price != 99999)
print("YES" if original_changed else "NO")

print("\nOriginal Laptops product:", product1.name, product1.price)
print("Copy Laptops product:", categories_copy["Laptops"][0].name, categories_copy["Laptops"][0].price)

print("\nDeep copy: Original structure does NOT change when copy is modified")