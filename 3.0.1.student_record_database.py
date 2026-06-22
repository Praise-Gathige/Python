ALLOWED_GRADES = ("A", "B", "C", "D", "E", "F")
FILE_NAME = "students.txt"

def load_db():

    students = []
    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                if line.strip():
                    id, name, grade = line.strip().split(",")
                    students.append({
                        'id': id,
                        'name': name,
                        'grade': grade
                        })
    except:
        pass
    return students


def save_db(students):
    with open(FILE_NAME, "w") as file:
        for s in students:
            file.write(f"{s['id']}, s{['name']}. s{['grade']}\n")



def add_student(students):
    id = input("Student ID: ")
    name = input("Student Name: ").title()
    grade = input("Student Grade (A, B, C, D, E, F): ").upper()

    if grade in ALLOWED_GRADES:
        students.append({'id': id, 'name': name, 'grade': grade})
        save_db(students)
        print("Student has been added.")
    else:
        print("Invalid grade.")


def find_student(students):
    id = input("Enter Student's ID to find: ")
    for s in students:
        if s['id'] == id:
            print(f"Found: {s['name']} - Grade: {s['grade']}")
            return
        else:
            print("Student not found.")

students = load_db()

while True:
    print("\n--- Students Database ---\n")
    print("1. Add Student\n2. Find Student\n3. Exit\n")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student(students)
    elif choice == "2":
        find_student(students)
    elif choice == "3":
        break
    else:
        print("Invalid choice!")













# Other option
# ALLOWED_GRADES = ("A", "B", "C", "D", "E", "F")
# FILE_NAME = "students.txt"

# def load_db():

#     students = []
#     with open(FILE_NAME, "r") as file:
#         for line in file:
#                     line = line.strip().split(",")
#                     dict = {
#                         'id': line[0],
#                         'name': line[1],
#                         'grade': line[2]
#                     }
#                     students.append(dict)


# def save_db(students):
#     for dict_item in students:
#          for key, value in dict_item.items():
#               with open(FILE_NAME, "w") as file:
#                    file.write(f"{key}, {value}")