# number = input()
#
# odd_sum = 0
# even_sum = 0
#
# for each_digit in number:
#     each_digit = int(each_digit)
#     if each_digit % 2 == 0:
#         even_sum += each_digit
#     else:
#         odd_sum += each_digit
# print(f"Odd sum = {odd_sum}, Even sum = {even_sum}")

def odd_and_even_sum(number):
    odd_sum = 0
    even_sum = 0
    for each_digit in number:
        if int(each_digit) % 2 == 0:
            even_sum += int(each_digit)
        else:
            odd_sum += int(each_digit)

    return f"Odd sum = {odd_sum}, Even sum = {even_sum}"

number = input()
print(odd_and_even_sum(number))
