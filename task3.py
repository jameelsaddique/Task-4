class Product:
    def __init__(self, prod_id, name, price, stock):
        self.prod_id = prod_id
        self.name = name
        self.price = price
        self.stock = stock

products = {
    "P001": Product("P001", "Laptop", 50000, 10),
    "P002": Product("P002", "Mouse", 800, 50),
    "P003": Product("P003", "Keyboard", 2000, 30),
    "P004": Product("P004", "Monitor", 8000, 15)
}

print("Product Inventory:")
print("Search by Product ID:")
pid = "P001"  # Default search product ID
if pid in products:
    p = products[pid]
    print(f"Product: {p.name}")
    print(f"Price: {p.price}")
    print(f"Stock: {p.stock}")
else:
    print("Product not found")