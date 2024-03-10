product = input()
quantity = int(input())

def calculate(product, quantity):
    if product == "coffee":
        return quantity * 1.50
    elif product == "coke":
        return  quantity * 1.40
    elif product == "water":
        return  quantity * 1.00
    elif product == "snacks":
        return  quantity * 2.00

result = calculate(product, quantity)
print(f"{result :.2f}")