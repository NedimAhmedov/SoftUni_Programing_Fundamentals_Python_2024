string_input = input().split()

while True:
    command = input()

    if command == "3:1":
        break

    split_command = command.split()
    action = split_command[0]

    if action == "merge":
        start_index = int(split_command[1])
        end_index = int(split_command[2])

        if start_index < 0:
            start_index = 0
        if end_index > len(string_input) - 1:
            end_index = len(string_input) - 1

        for index, string in enumerate(string_input):
            if index in range(start_index + 1, end_index + 1):
                string_input[start_index] += string_input[index]
        for index in range(end_index, start_index, -1):
            string_input.pop(index)


    if action == "divide":
        index = int(split_command[1])
        partitions = int(split_command[2])

        if partitions > len(string_input[index]):
            step = 1
        else:
            step = len(string_input[index]) // partitions
        divide_part = string_input.pop(index)
        start = 0

        for parts in range(partitions):
            if parts == partitions - 1:
                string_input.insert(index, divide_part[start::])
                break
            else:
                string_input.insert(index, divide_part[start: start + step:])
            start += step
            index += 1
print(*string_input)
