def proces_to_do():
    notes = []

    while True:
        command = input()

        if command == "End":
            break

        notes.append(command)

    sorted_notes = sorted(notes, key=lambda x: int(x.split("-")[0]))
    sorted_notes = [command.split("-")[1] for command in sorted_notes]

    return sorted_notes
print(proces_to_do())

