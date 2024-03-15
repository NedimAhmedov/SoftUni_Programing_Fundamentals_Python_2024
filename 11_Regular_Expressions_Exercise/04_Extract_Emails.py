import re

text = input()

regex = r"\s(([a-z0-9]+[a-z0-9\.\-\_]*)@([a-z\-]+)(\.[a-z]+)+)\b"  # s- празно пространство, * означава 0 или повече пъти

matches = re.findall(regex, text)

for email in matches:
    print(email[0])