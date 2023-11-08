from typing import TextIO

# student1: list[str] = ["Vic", "Vu"]
# student2: list[str] = ["Sue", "Salias"]
student1: dict[str, str] = {"first_name": "Vic", "last_name": "Vu"}
student2: dict[str, str] = {"first_name": "Sue", "last_name": "Salias"}
students: list[dict[str]] = [student1, student2]
print(students)

student_first_name = input("Enter the student's first name: ")
student_last_name = input("Enter the student's last name: ")
student_data = {"first_name": student_first_name, "last_name": student_last_name}
students.append(student_data)


student_last_name = input("Please enter last name to remove: ")
print(id(students))
print(id(students[:]))
for student in students[:]:
    if student_last_name == student["last_name"]:
        students.remove(student)


for student in students:
    print(f'{student["first_name"]} {student["last_name"]}')

FILE_NAME = "MyData.csv"
file_obj: TextIO = open(FILE_NAME, "w")
for student in students:
    file_obj.write(f'{student["first_name"]},{student["last_name"]}\n')
file_obj.close()


students = []
print(students)

file_obj: TextIO = open(FILE_NAME, "r")
for line in file_obj.readlines():
    student_data = line.strip().split(",")
    student_dict = {"first_name": student_data[0], "last_name": student_data[1]}
    students.append(student_dict)


for student in students:
    print(f'{student["first_name"]} {student["last_name"]}')

for student in students:
    student["gpa"] = 4.0

print(students)

for student in students:
    student["gpa"] = 3.8
print(students)
