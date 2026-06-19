print(f'Complete the test below to test your IQ.')
name = input('Enter your name: ').title()
print(f'Welcome to my test {name}')

score = 0

Q1 = print(input(f'Q1. What is the capital city of Kenya? ').title())
nairobi = Q1
if Q1 == nairobi:
    print('Correct')
    score = 1
else:
    print('Incorrect')


Q2 = print(int(input(f'Q2. How many counties are there in Kenya? ')))
Q2 = 47
if Q2 == 47:
    print('Correct')
    score = 2
else:
    print('Incorrect')


Q3 = print(input(f'Q3. Who is the current president of Kenya? ').title())
Ruto = Q3
if Q3 == Ruto:
    print('Correct')
    score = 3
else:
    print('Incorrect')

print(f'You have completed the test and your score is {score}')
