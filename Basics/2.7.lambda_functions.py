greet = lambda x: f"Hello {x}"
print(greet("keith"))

#lambda is used in the filter() and sort() inbuilt functions

ages = [18, 16, 10, 23, 25]

adults = list(filter(lambda x: x >= 18, ages))
print(adults)

#you can either us print(list(adults)) or list(filter(lambda x: x >= 18, ages))

upcoming_years = list(map(lambda x: x * 10, ages))

print(upcoming_years)