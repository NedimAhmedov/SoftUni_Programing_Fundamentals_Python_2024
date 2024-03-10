needed_experience = float(input())
battles_count = int(input())

total_earned_experience = 0

for each_battle in range(1, battles_count + 1):
    earned_experience_per_battle = float(input())

    total_earned_experience += earned_experience_per_battle

    if each_battle % 3 == 0:
        total_earned_experience += earned_experience_per_battle * 0.15

    if each_battle % 5 == 0:
        total_earned_experience -= earned_experience_per_battle * 0.1

    if each_battle % 15 == 0:
        total_earned_experience += earned_experience_per_battle * 0.5

    if total_earned_experience >= needed_experience:
        break

if total_earned_experience >= needed_experience:
    print(f"Player successfully collected his needed experience for {each_battle} battles.")
else:
    neededExperience = needed_experience - total_earned_experience
    print(f"Player was not able to collect the needed experience, {neededExperience :.2f} more needed.")