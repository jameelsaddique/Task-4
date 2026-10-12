class Resource:
    def __init__(self):
        print("Resource created")

    def __del__(self):
        print("Resource destroyed")


# A. Multiple References
print("=== Task 2A: Multiple References ===")
r1 = Resource()
r2 = r1
print(f"r1 id: {id(r1)}, r2 id: {id(r2)}")
print("Both r1 and r2 point to same object")
del r1
print("After del r1, r2 still exists")
del r2
print("After del r2, object fully destroyed\n")


# B. Reassigning a Reference
print("=== Task 2B: Reassigning a Reference ===")
r3 = Resource()
print(f"r3 created, id: {id(r3)}")
r4 = r3
print("r4 assigned to same object")
r3 = Resource()  # Reassign r3 to new object
print(f"r3 reassigned to new object, id: {id(r3)}")
print(f"r4 still points to old object (will be garbage collected)")
del r3, r4
print("Both deleted\n")


# C. Object Inside a Function
print("=== Task 2C: Object Inside a Function ===")

def create_resource():
    r = Resource()
    return r

r5 = create_resource()
print(f"Resource created in function, id: {id(r5)}")
print("Function returned, r5 still references it")
del r5
print("r5 deleted\n")