from typing import TextIO

import json

student1: dict[str, str | float] = {"first_name": "Vic", "last_name": "Vu", "gpa": 4.0}
student2: dict[str, str | float] = {
    "first_name": "Sue",
    "last_name": "Salias",
    "gpa": 4.0,
}
students: list[dict[str]] = [student1, student2]

FILE_NAME_CSV = "MyData.csv"
FILE_NAME_JSON = "MyData.json"

file_obj: TextIO = open(FILE_NAME_CSV, "w")
for student in students:
    file_obj.write(f"{student['first_name']},{student['last_name']},{student['gpa']}\n")
file_obj.close()

file_obj = open(FILE_NAME_JSON, "w")
json.dump(students, file_obj)
file_obj.close()

students = []
file_obj = open(FILE_NAME_CSV, "r")
for line in file_obj.readlines():
    student_data = line.strip().split(",")
    students.append(
        {
            "first_name": student_data[0],
            "last_name": student_data[1],
            "gpa": float(student_data[2]),
        }
    )
file_obj.close()
print(students)

students = []
file_obj = open(FILE_NAME_JSON, "r")
# For some reason, pycharm gives me a weird yellow line here
students = json.load(file_obj)
file_obj.close()
print(students)
