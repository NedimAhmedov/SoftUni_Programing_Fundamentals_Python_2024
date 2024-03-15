import re

strings = input()

while strings:
    regex = r"\d+"
    matches = re.findall(regex, strings)
    if matches:
        print(" ".join(matches), end=" ")
    strings = input()
