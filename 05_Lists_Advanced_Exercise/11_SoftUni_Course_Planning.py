lessons = list(input().split(", "))

while True:
    command = input()

    if command == "course start":
        for i, lesson in enumerate(lessons):
            print(f"{i + 1}.{lesson}")
        break

    split_command = command.split(":")
    action = split_command[0]
    lesson_title = split_command[1]

    if action == "Add":
        if lesson_title not in lessons:
            lessons.append(lesson_title)

    elif action == "Insert":
        index = int(split_command[2])
        if lesson_title not in lessons:
            lessons.insert(index, lesson_title)

    elif action == "Remove":
        if lesson_title in lessons:
            lessons.remove(lesson_title)
        if f"{lesson_title}-Exercise" in lessons:
            lessons.remove(f"{lesson_title}-Exercise")

    elif action == "Swap":
        second_lesson = split_command[2]
        if lesson_title in lessons and second_lesson in lessons:
            first_lesson_index = lessons.index(lesson_title)
            second_lesson_index = lessons.index(second_lesson)
            lessons[first_lesson_index], lessons[second_lesson_index] = lessons[second_lesson_index], lessons[first_lesson_index]
            if f"{lesson_title}-Exercise" in lessons:
                lessons.remove(f"{lesson_title}-Exercise")
                lesson_index = lessons.index(lesson_title)
                lessons.insert(lesson_index + 1, f"{lesson_title}-Exercise")
            if f"{second_lesson}-Exercise" in lessons:
                lessons.remove(f"{second_lesson}-Exercise")
                lesson_index = lessons.index(second_lesson)
                lessons.insert(lesson_index + 1, f"{second_lesson}-Exercise")

    elif action == "Exercise":
        if lesson_title not in lessons:
            lessons.append(lesson_title)
            current_ex = lesson_title + "-Exercise"
            lessons.append(current_ex)
        elif lesson_title in lessons and f"{lesson_title}-Exercise" not in lessons:
            lesson_index = lessons.index(lesson_title)
            lessons.insert(lesson_index + 1, f"{lesson_title}-Exercise")