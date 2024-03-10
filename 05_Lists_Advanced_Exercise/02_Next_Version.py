version = list(map(int, input().split(".")))

version[-1] += 1
for index in range(len(version) -1, 0, -1):  #  почваме от последния елемент -1, стигаме до елемент 0(без да е включен) и вървим със стъпка -1(назад)
    if version[index] > 9:
        version[index] = 0
        version[index - 1] += 1

print(".".join(map(str, version)))