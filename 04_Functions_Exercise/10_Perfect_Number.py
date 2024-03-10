def perfect_number(number):
    divisor_sum = 0

    for divisor in range(1, number):
        if number % divisor == 0:
            divisor_sum += divisor

    if divisor_sum == number:
        return  "We have a perfect number!"
    else:
        return  "It's not so perfect."

num = int(input())
print(perfect_number(num))