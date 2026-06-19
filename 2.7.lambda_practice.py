# The Quick Calculator
multiplier = lambda x, y: x * y
print(multiplier(6,7)) 


# The Name Sanitizer
names = [" alice ", "BOB", " charlie"]

clean_names = list(map(lambda name: name.strip().title(), names))

print(clean_names)



# Boss Challenge: The HR Database Filter

employees = [
    {"name": "John", "role": "Developer", "salary": 65000},
    {"name": "Sarah", "role": "Designer", "salary": 72000},
    {"name": "Mike", "role": "Developer", "salary": 80000},
    {"name": "Emma", "role": "Manager", "salary": 95000}
]

devs_only = list(filter(lambda emp: emp["role"] == "Developer", employees))

print(devs_only)