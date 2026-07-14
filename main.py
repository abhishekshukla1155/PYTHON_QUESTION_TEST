
import student_utils
import json

students = []

for i in range(3):
    # Ask for student name
    name = input(f"Hey, what's the name of student {i+1}? ")

    marks = []

    for j in range(3):
        while True:
            try:
                mark = float(input(f"Enter subject {j+1} mark for {name}: "))
                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print("Oops, that's not a valid mark. Please try again!")
            except ValueError:
                print("Hmm, that's not a number. Please try again!")

    students.append({'name': name, 'marks': marks})

for student in students:
    avg = student_utils.calculate_average(*student['marks'])
    grade = student_utils.get_grade(avg)
   