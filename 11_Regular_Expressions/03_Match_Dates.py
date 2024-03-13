import re

regex = r"(\d{2})([-./])([A-Z][a-z]{2})\2(\d{4})"

date = input()

matches = re.findall(regex, date)
for match in matches:
    print(f"Day: {match[0]}, Month: {match[2]}, Year: {match[3]}")
