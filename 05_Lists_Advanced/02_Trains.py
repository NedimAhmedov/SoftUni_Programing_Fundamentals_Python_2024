wagon = [0] * int(input())

while True:
    command = input().split()

    if command[0] == "End":
        print(wagon)
        break

    if command[0] == "add":
        wagon[-1] += int(command[1])

    if command[0] == "insert":
        index = int(command[1])
        number_of_people = int(command[2])
        wagon[index] += number_of_people

    if command[0] == "leave":
        index = int(command[1])
        number_of_people = int(command[2])
        wagon[index] -= number_of_people

