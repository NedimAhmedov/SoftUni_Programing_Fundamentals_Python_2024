targets_sequences = list(map(int, input().split()))

while True:
    command = input()
    if command == "End":
        print(*targets_sequences, sep="|")
        break

    split_command = command.split()
    action = split_command[0]

    if action == "Shoot":
        index = int(split_command[1])
        power = int(split_command[2])
        if 0 <= index < len(targets_sequences):
            targets_sequences[index] -= power
            if targets_sequences[index] <= 0:
                targets_sequences.remove(targets_sequences[index])

    elif action == "Add":
        index = int(split_command[1])
        value = int(split_command[2])
        if 0 <= index < len(targets_sequences):
            targets_sequences.insert(index, value)
        else:
            print("Invalid placement!")

    elif action == "Strike":
        index = int(split_command[1])
        radius = int(split_command[2])

        start = index - radius
        end = index + radius

        if start >= 0 and end < len(targets_sequences):
            del targets_sequences[start: end + 1]
        else:
            print("Strike missed!")

