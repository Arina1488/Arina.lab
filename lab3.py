students = []

while True:
    name = input("Enter student name: ")
    if name == "stop":
        break
    grade = input("Enter student grade: ")
    if grade == "stop":
        break


    try:
       grade = int(grade)
    except ValueError:
       print("Grade must be the number!")
       continue

    students.append({"name": name, "grade": grade})

print("List of students:")
for student in students:
    print(f"{student['name']} - {student['grade']}")


avg = sum(student["grade"] for student in students) / len(students)

print(f"Average grade: {avg}")

excellent = []
for student in students:
    if student['grade'] >=10 and student['grade'] <=12:
       excellent.append(student)

print(f"Excellent students: {len(excellent)}")
for student in excellent:
    print(f"{student['name']} - {student['grade']}")

well = []
for student in students:
    if student['grade'] >= 7 and student['grade'] <= 9:
        well.append(student)

print(f"Well students: {len(well)}")
for student in well:
    print(f"{student['name']} - {student['grade']}")


notbad = []
for student in students:
    if student['grade'] >=4 and student['grade'] <=6:
       notbad.append(student)

print(f"Notbad students: {len(notbad)}")
for student in notbad:
    print(f"{student['name']} - {student['grade']}")


unsubmitted = []
for student in students:
    if student['grade'] >=1 and student['grade'] <=3:
       unsubmitted.append(student)

print(f"Unsubmitted students: {len(unsubmitted)}")
for student in unsubmitted:
    print(f"{student['name']} - {student['grade']}")
