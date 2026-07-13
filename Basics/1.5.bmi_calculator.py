weight_in_kg = input("What is your weight?(In kilograms): ")
weight = float(weight_in_kg)

height_in_m = input("What is you height?(In metres eg. 1.75): ")
height = float(height_in_m)

bmi = weight / (height ** 2)

print(f"\nYour body mass index is {bmi:.2f}")

if bmi < 18.5:
    print("Category: Underweight")
elif bmi < 25:
    print("Category: Normal weight")
elif bmi < 30:
    print("Category: Overweight")
else:
    print("Category: Obese")

