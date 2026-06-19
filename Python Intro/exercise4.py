print("Grades Calculator")
print('Hello. Input your name and your subject marks accordingly')
name = input('Enter name: ')


maths = int(input("maths: "))
if maths > 100:
    print('invalid. Enter a number from 0 and 100')
    maths = int(input("maths: "))

elif maths < 0:
    print('invalid. Enter a number from 0 and 100')
    maths = int(input("maths: "))

english = int(input("english: "))
if english > 100:
    print('invalid')
    english = int(input("english: "))

elif english < 0:
    print('invalid')
    english = int(input("english: "))


physics = int(input("physics: "))
if physics > 100:
    print('invalid')
    physics = int(input("physics: "))

elif physics < 0:
    print('invalid')
    physics = int(input("physics: "))


kiswahili = int(input("kiswahili: "))
if kiswahili > 100:
    print('invalid')
    kiswahili = int(input("kiswahili: "))

elif (kiswahili < 0):
    print('invalid')
    kiswahili= int(input("kiswahili: "))


history = int(input("history: "))
if history > 100:
    print('invalid')
    history = int(input("history: "))

elif history < 0:
    print('invalid')
    history= int(input("history: "))


#write a programme that grades student based on average

# 0-39 E
# 40-50 D
# 51-60 C
# 61-78 B
# 79-100 A

sum = maths + english + physics + kiswahili + history
average = sum/5

if average > 78:
    print(f'{name}, your mean is {average} and your overall grade is A')
elif average > 60:
    print(f'{name}, your mean is {average} and your overall grade is B')
elif average > 50:
    print( f'{name}, your mean is {average} and your overall grade is C')
elif average > 39:
    print( f'{name}, your mean is {average} and your overall grade is D')
else:
    print( f'{name}, your mean is {average} and your overall grade is E')







