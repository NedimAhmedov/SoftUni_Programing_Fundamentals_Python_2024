waiting_people = int(input())
lift_current_state = list(map(int, input().split()))

for i in range(len(lift_current_state)):
    can_load = min(4 - lift_current_state[i], waiting_people)
    lift_current_state[i] += can_load
    waiting_people -= can_load

if waiting_people > 0:
    print(f"There isn't enough space! {waiting_people} people in a queue!")
elif len([cart for cart in lift_current_state if cart < 4]) > 0:
    print("The lift has empty spots!")

print(" ".join([str(cart) for cart in lift_current_state]))