first_integer = int(input())
second_integer = int(input())
third_integer = int(input())
fourth_integer = int(input())

result = ((first_integer + second_integer) // third_integer) * fourth_integer  # целочислено деление, защото при деление ще се получи float

print(result)