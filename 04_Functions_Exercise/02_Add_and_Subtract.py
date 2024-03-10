def sum_numbers(first, second):
    return first + second

def subtract(result, third):
    return result - third

def add_and_subtract(first, second, third):
    result = sum_numbers(first, second)
    return subtract(result, third)

first = int(input())
second = int(input())
third = int(input())
print(add_and_subtract(first, second, third))


