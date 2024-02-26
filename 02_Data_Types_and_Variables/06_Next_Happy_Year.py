# year = int(input())
# while True:
#     year += 1
#     is_happy_year = True
#     already_found_digits = ""
#     for digits in str(year):
#         if digits in already_found_digits:
#             is_happy_year = False
#             break
#         already_found_digits += digits
#     if is_happy_year:
#         break
# print(year)

year = int(input())
while True:
    year += 1
    year_as_string = str(year)
    if len(year_as_string) == len(set(year_as_string)):  # решение със сет
        break
print(year)
