number_of_students = int(input())
number_of_lectures = int(input())
additional_bonus = int(input())

max_pointed_student = 0
max_pointed_student_attendance = 0

for each_student in range(1, number_of_students + 1):
    each_student_attendance = int(input())
    each_student_max_points = each_student_attendance / number_of_lectures * (5 + additional_bonus)
    if each_student_max_points > max_pointed_student:
        max_pointed_student = each_student_max_points
        max_pointed_student_attendance = each_student_attendance
print(f"Max Bonus: {round(max_pointed_student)}.")
print(f"The student has attended {max_pointed_student_attendance} lectures.")


