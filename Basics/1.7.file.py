file = open("report.txt", "w")
file.write("Praise")

file.close()

report = open("report.txt", "r")
content = report.read()
print(content)

# with open() handles both opening and closing for us
with open("report.txt", "w") as file:
    file.write("We are in a classroom\n")
    file.write("Type a letter to the director")

#print(file.closed)
#print(report.closed)

with open("report.txt", "a") as report:
    report.write("\nappending data")