#Part 1 - Student List(Lists)
students = []
print("Enter 5 student names.")
for i in range(5):
    name = input(f"Enter student {i + 1}: ")
    students.append(name)

print("\nList of all students:", students)
print("Total number of students: ", len(students))


#Part 2 - Registration Numbers(Tuples)
reg_numbers = ("REG101", "REG102", "REG103", "REG104", "REG105")

print("\nStudent Registration Details:")
for i in range (5):
    print(f"Name: {students[i]} | Reg No: {reg_numbers[i]}")


#Part 3 - Student Marks(Dictionaries)
marks = {}

print("\nEnter marks for each student: ")
for student in students:
    score = int(input(f"Enter marks for {student}: "))
    marks[student] = score

print("\nStudent Marks:", marks)

#Part 4 - Top Student
highest_mark = max(marks.values())




#Part 5 - Average Score
average = sum(marks.values()) / len(marks)
print(f"Average score of all students: {average:.2f}")