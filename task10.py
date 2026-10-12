class Order:
    def __init__(self, order_id, customer_name, products, total_amount):
        self.order_id = order_id
        self.customer_name = customer_name
        self.products = products
        self.total_amount = total_amount

orders = [
    Order("O001", "Ali", ["Laptop", "Mouse"], 50800),
    Order("O002", "Sara", ["Keyboard", "Monitor"], 10000),
    Order("O003", "Ahmed", ["Laptop", "Keyboard"], 130000)
]

print("Original Orders:")
for o in orders:
    print(f"Order {o.order_id}: {o.customer_name}, Products: {o.products}, Total: {o.total_amount}")

import copy
# Deep copy of complete order list
orders_backup = copy.deepcopy(orders)

# Modify a product inside the backup
orders_backup[0].products[0] = "Gaming Laptop"
orders_backup[0].total_amount = 60000

print("\n\nAfter modifying backup:")
print("Original order data unchanged:")
print(f"Original Order O001 products: {orders[0].products}")
print(f"Original Order O001 total: {orders[0].total_amount}")

print("\nBackup modified data:")
print(f"Backup Order O001 products: {orders_backup[0].products}")
print(f"Backup Order O001 total: {orders_backup[0].total_amount}")

print("\nDeep copy: Original order data is unchanged when backup is modified")