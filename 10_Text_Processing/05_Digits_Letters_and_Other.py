digits = ""
letters= ""
characters = ""

text_string = input()

for each_char in text_string:
    if each_char.isdigit():
        digits += each_char
    elif each_char.isalpha():
        letters += each_char
    else:
        characters += each_char

print(digits)
print(letters)
print(characters)