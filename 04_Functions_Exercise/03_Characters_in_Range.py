# char_one = input()
# char_two = input()
#
# char_list = []
#
# for each_char in range(ord(char_one) + 1, ord(char_two)):
#     char_list.append(chr(each_char) + "")
# print(*char_list)

def char_func(char_one, char_two):
    result = ""
    for each_char in range(ord(char_one) + 1, ord(char_two)):
        result += chr(each_char) + " "

    return result


first_char = input()
second_char = input()
print(char_func(first_char, second_char))
