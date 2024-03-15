import re

regex = r"(w{3}\.[A-Za-z0-9\-\.]+\.[a-z]+)"

line = input()

while line:
    match = re.search(regex, line)
    if match:
        valid_url = match.group(1)
        print(valid_url)

    line = input()