numbers_as_list = input().split()
numbers_to_remove = int(input())

numbers_as_integer = []
for numbers in numbers_as_list:
    numbers_as_integer.append(int(numbers))

for cycles in range(numbers_to_remove):
    numbers_as_integer.remove(min(numbers_as_integer))  # с min намираме най-малкото число в листа и го махаме от листа
print(*numbers_as_integer, sep=", ")  # с * преди листа махаме скобите на листа, а с sep= разделяма както искаме
