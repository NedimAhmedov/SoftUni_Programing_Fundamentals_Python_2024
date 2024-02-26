command = input()
while command != "End":
    if command != "SoftUni":
        new_string = ""
        for characters in command:
            new_string += characters * 2
        print(new_string)
    command = input()