Profile = {
    "Name" : "Keith",
    "Age" : 19,
    "Isstudent" : True
}

print(Profile)
print(Profile["Name"])

Profile["Name"] = "Tim"

Profile["Location"] = "Thika"
del Profile["Name"]
a = Profile.pop("Age")
b = Profile.popitem()
print(Profile)
print(a)
print(b)