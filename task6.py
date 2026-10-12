cart = [
    ["Laptop", 1],
    ["Mouse", 2],
    ["Keyboard", 1]
]

import copy

# Shallow copy
shallow_cart = cart.copy()

# Deep copy
deep_cart = copy.deepcopy(cart)

print("Original cart:")
for item in cart:
    print(f"  {item}")

# Modify quantity in shallow copy
shallow_cart[0][1] = 3
print("\nAfter modifying shallow copy quantity:")
print("Original cart:", cart)
print("Shallow cart:", shallow_cart)

# Reset cart
cart = [
    ["Laptop", 1],
    ["Mouse", 2],
    ["Keyboard", 1]
]

# Modify quantity in deep copy
deep_cart[2][1] = 5
print("\nAfter modifying deep copy quantity:")
print("Original cart:", cart)
print("Deep cart:", deep_cart)

print("\nShallow copy affects original (nested list is shared)")
print("Deep copy does NOT affect original (independent nested lists)")