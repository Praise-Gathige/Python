# program that checks whether a number is even or odd

def even_or_odd(number):
    if number % 2 == 0:
        return 'Even'
    else:
        return 'Odd'

num = int(input('Enter Number: '))
result = even_or_odd(num)
print(f'The number {num} is {result}')
