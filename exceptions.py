import json
from json import JSONDecodeError
from typing import TextIO

FILENAME = "data.json"
file: TextIO = None
students: list[dict[str, str]] = []
try:
    file = open(FILENAME, "r")
    students = json.load(file)
except FileNotFoundError as e:
    print("The file was not found, creating it...")
    file = open(FILENAME, "w")
    json.dump(students, file)
except JSONDecodeError as e:
    print("JSON file was invalid, resetting it...")
    file = open(FILENAME, "w")
    json.dump(students, file)
except Exception as e:
    print("There was a non-specific error!")
    print("---Technical Error Message---")
    print(e, e.__doc__, type(e), sep="\n")
finally:
    if file and not file.closed:
        file.close()

while True:
    try:
        student_first_name = input("Enter student first name: ")
        if not student_first_name.isalpha():
            raise ValueError("The first name must be alphabetic")
        break
    except ValueError as e:
        print(e)


invalid = True
while invalid:
    try:
        student_last_name = input("Enter student last name: ")
        if not student_last_name.isalpha():
            raise ValueError("The last name must be alphabetic")
        invalid = False
    except ValueError as e:
        print(e)

students.append({"first_name": student_first_name, "last_name": student_last_name})


try:
    file = open(FILENAME, "w")
    json.dump(students, file)
except Exception as e:
    print("There was a non-specific error!")
    print("---Technical Error Message---")
    print(e, e.__doc__, type(e), sep="\n")
finally:
    if file and not file.closed:
        file.close()
