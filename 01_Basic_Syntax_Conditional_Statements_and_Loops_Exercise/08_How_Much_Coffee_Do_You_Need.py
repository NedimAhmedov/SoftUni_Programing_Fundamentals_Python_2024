coffee_counter = 0
command = input()
while command != "END":
    if command.lower() == "coding" \
            or command.lower() == "dog" \
            or command.lower() == "cat" \
            or command.lower() == "movie":  # проверяваме командата, дали я има, но преобърната в малко букви
        if command.islower():  # тук вече проверяваме, дали самата команда е с малки или с големи букви
            coffee_counter += 1
        elif command.isupper():
            coffee_counter += 2
    command = input()
if coffee_counter > 5:
    print("You need extra sleep")
else:
    print(coffee_counter)

