
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print("Sum :", add(x, y))
print("Difference :", subtract(x, y))
print("Product :", multiply(x, y))
print("Quotient :", divide(x, y))