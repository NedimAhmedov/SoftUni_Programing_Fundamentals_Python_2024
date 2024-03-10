number_of_rooms = int(input())
left_chair = 0
for each_room in range(1, number_of_rooms + 1):
    command = input().split()
    if int(len(command[0])) < int(command[1]):
        print(f"{abs(int(len(command[0])) - int(command [1]))} more chairs needed in room {each_room}")
        left_chair -= int(command[1]) - int(len(command[1]))
    else:
        left_chair += abs(int(command[1]) - int(len(command[0])))
if left_chair >= 0:
    print(f"Game On, {left_chair} free chairs left")