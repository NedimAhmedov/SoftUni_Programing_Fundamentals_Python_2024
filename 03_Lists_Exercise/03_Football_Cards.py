#print([f"A-{number}" for number in range(1,12)])  # list comprehension, за да не пишвм едно по едно всяко
#print([f"B-{number}" for number in range(1,12)])  # list comprehension, за да не пишвм едно по едно всяко

team_a = ['A-1', 'A-2', 'A-3', 'A-4', 'A-5', 'A-6', 'A-7', 'A-8', 'A-9', 'A-10', 'A-11']
team_b = ['B-1', 'B-2', 'B-3', 'B-4', 'B-5', 'B-6', 'B-7', 'B-8', 'B-9', 'B-10', 'B-11']

card_list = input().split(" ")
terminated_game = False

for each_payer in card_list:
    if each_payer in team_a:
        team_a.remove(each_payer)
    elif each_payer in team_b:
        team_b.remove((each_payer))
    if len(team_a) < 7 or len(team_b) < 7:
        terminated_game = True
        break
print(f"Team A - {len(team_a)};", end=" ")
print(f"Team B - {len(team_b)}")
if terminated_game:
    print("Game was terminated")