days_of_plunder = int(input())
daily_plunder = int(input())
expected_plunder = float(input())

sum_plunder = 0

for each_day in range(1, days_of_plunder + 1):
    sum_plunder += daily_plunder
    if each_day % 3 == 0:
        sum_plunder += daily_plunder * 0.5
    if each_day % 5 == 0:
        sum_plunder -= sum_plunder * 0.3

if sum_plunder >= expected_plunder:
    print(f"Ahoy! {sum_plunder :.2f} plunder gained.")
else:
    left_percent = (sum_plunder / expected_plunder) * 100
    print(f"Collected only {left_percent :.2f}% of the plunder.")
