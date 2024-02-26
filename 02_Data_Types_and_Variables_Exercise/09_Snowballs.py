import math

number_of_snowballs = int(input())

best_weight = 0
best_needed_time = 0
best_quality = 0
best_quality_snowball = 0

for each_snowball in range(number_of_snowballs):
    weight = int(input())
    needed_time = int(input())
    quality = int(input())
    quality_current_snowball = (weight / needed_time) ** quality
    if quality_current_snowball > best_quality_snowball:
        best_weight = weight
        best_needed_time = needed_time
        best_quality = quality
        best_quality_snowball = quality_current_snowball
print(f"{best_weight} : {best_needed_time} = {math.floor(best_quality_snowball)} ({best_quality})")


