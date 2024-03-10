course_dict = {}

while True:
    command = input()
    if command == "end":
        break

    split_command = command.split(" : ")
    course_name = split_command[0]
    student_name = split_command[1]

    if course_name not in course_dict:
        course_dict[course_name] = []  # създаваме празен списък, в който ще съхраняваме имената
    course_dict[course_name].append(student_name)

for each_course, each_student in course_dict.items():
    print(f"{each_course}: {len(course_dict[each_course])}")
    for student in each_student:
        print(f"-- {student}")