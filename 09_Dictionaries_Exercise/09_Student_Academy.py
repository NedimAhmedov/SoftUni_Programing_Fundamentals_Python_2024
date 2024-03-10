student_dict = {}
student_count = int(input())

for each_student in range(student_count):
    student_name = input()
    student_grade = float(input())

    if student_name not in student_dict:
        student_dict[student_name] = []
    student_dict[student_name].append(student_grade)

for student, grade in student_dict.items():
    avg_grade = sum(student_dict[student]) / len(student_dict[student])
    if avg_grade >= 4.5:
        print(f"{student} -> {avg_grade :.2f}")