ALLOWED_GRADES = ('A', 'B', 'C', 'D', 'E', 'F')

def load_db():
    students = []
    try:
        with open("students.txt", "r") as file:
            for line in file:
                if line.strip():
                    student_id, name, grade = line.strip().split(',')
    except FileNotFoundError:

        open("students.txt", "w").close()
    return students


def save_db(students):
    with open("students.txt", "w") as file:
        for student in students:
            file.write(f"{student["id"]}, {student["name"]}, {student["grade"]}\n")


def add_student(students):
    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    grade = input("Enter Grade (A, B, C, D, E, F): ").upper()

    if grade in ALLOWED_GRADES:
        students.append({"id": student_id, "name": name, "grade": grade})
        save_db(students)
        print("Student added successfully.")
    else:
        print("Invalid grade. Student not added.")


def find_student(students):
    lookup = input("Enter student's ID: ")

    for student in students:
        if student["id"] == lookup:
            print(f"Found: ID: {student["id"]}, Name: {student["name"]}, Grade: {student["grade"]}")
            return student
    print("Student not found.")
    return None


def main():
    while True:
        students = load_db()
        print("\n--- Student Database ---")
        print("1. Add Student\n2. Find Student\n3. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            add_student(students)
        elif choice == "2":
            find_student(students)
        elif choice == "3":
            break


main()
