lines_number = int(input())
sum = 0
for cycles in range(lines_number):
    char = input()
    sum += ord(char) # с ord взимме аски кода на char
print(f"The sum equals: {sum}")