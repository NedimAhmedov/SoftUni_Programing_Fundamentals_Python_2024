def positive_numbers_func(number_list):
    return ", ".join([number for number in number_list if int(number) >= 0])


def negative_numbers_func(number_list):
    return ", ".join([number for number in number_list if int(number) < 0])


def even_number_func(number_list):
    return ", ".join([number for number in number_list if int(number) % 2 == 0])


def odd_number_func(number_list):
    return ", ".join([number for number in number_list if int(number) % 2 != 0])


numbers = input().split(", ")
print(f"Positive: {positive_numbers_func(numbers)}")
print(f"Negative: {negative_numbers_func(numbers)}")
print(f"Even: {even_number_func(numbers)}")
print(f"Odd: {odd_number_func(numbers)}")
