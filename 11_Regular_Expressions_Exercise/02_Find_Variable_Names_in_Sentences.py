import re

strings = input()


regex = r"\b_([A-Za-z0-9]+)\b"
matches = re.findall(regex, strings)
print(",".join(matches), end=" ")
