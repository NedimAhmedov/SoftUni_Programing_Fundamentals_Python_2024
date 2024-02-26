gifts_names = input().split()

command = input()
while command != "No Money":
    command = command.split()
    if "OutOfStock" in command:
        for i in range(len(gifts_names)):
            if command[1] in gifts_names[i]:
                gifts_names[i] = "None"
    elif "Required" in command:
        for i in range(len(gifts_names)):
            if i == int(command[2]):
                gifts_names[i] = command[1]
    elif "JustInCase" in command:
        for i in range(len(gifts_names)):
            gifts_names[-1] = command[1]

    command = input()

while "None" in gifts_names:
    gifts_names.remove("None")

print(*gifts_names)