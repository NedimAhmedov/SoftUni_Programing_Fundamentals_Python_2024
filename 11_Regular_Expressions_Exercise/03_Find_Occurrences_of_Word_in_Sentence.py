import re

text = input()
searched_word = input()

regex = fr"(?i)\b{searched_word}\b"

match = re.findall(regex, text)
print(len(match))
