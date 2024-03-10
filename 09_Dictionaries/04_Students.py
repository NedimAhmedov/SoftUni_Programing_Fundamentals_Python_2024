student_info = []
course_to_search = None
while True:
    command = input()
    if ":" not in command:
        course_to_search = command
        break

    split_command = command.split(":")
    name = split_command[0]
    student_id = split_command[1]
    course = split_command[2]

    student_info.append({'name': name, 'ID': student_id, 'course': course})  # създава списък с множество речници

for each_student in student_info:
    if course_to_search.startswith(each_student['course'][0:3]):  #  проверяваме съвпадение в първите 3 букви
        print(f"{each_student['name']} - {each_student['ID']}")
