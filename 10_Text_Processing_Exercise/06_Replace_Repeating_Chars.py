text = input()
new_text = ""
last_added_char = ""
for each_char in text:
    if each_char not in last_added_char:
        new_text += each_char
        last_added_char = each_char
print(new_text)