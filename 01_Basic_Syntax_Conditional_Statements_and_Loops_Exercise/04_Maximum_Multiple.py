divisor = int(input())
boundary = int(input())

for cycles in range(boundary, divisor -1, -1):
    if cycles % divisor == 0:
        break
print(cycles)