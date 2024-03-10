def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def factorial_division(num1, numb2):
    result1 = factorial(num1)
    result2 = factorial(numb2)
    division_result = result1 / result2
    return f"{division_result :.2f}"


num1 = int(input())
num2 = int(input())
print(factorial_division(num1, num2))
