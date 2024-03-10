list_of_numbers = input().split(", ")
#list_of_numbers_as_int = list(map(int, input().split(", "))) - list comprehension
list_of_numbers_as_int = []
for each_number in list_of_numbers:
    list_of_numbers_as_int.append(int(each_number))


def palindrome_numbers(number):
    result = ""
    for each_integer in list_of_numbers_as_int:
        if str(each_integer) == str(each_integer)[::-1]:  # със slice notation обръщаме числата
            result += "True \n"
        else:
            result += "False \n"
    return result


print(palindrome_numbers(list_of_numbers_as_int))
