# Lab12

# 1. Define a function that will not require additional arguments, but will calculate addition between numbers.

def addition(a, b):
    print(a + b)
#example
addition(2, 5)

# 2. Define a function that will require additional arguments, but will calculate multiplication between numbers.
# 3. Define a function that will require additional arguments, but will calculate division between numbers.
# Program containing both tasks 2 and 3:

def calculate(a, b, symbol):
    if symbol == '*':
        print(f'The multiplication of these two numbers results in: {a * b}')
    elif symbol == '//':
        print(f'The division of these two numbers results in: {a // b}')
    elif symbol == '**':
        print(f'Number 1, to the power of number 2, results in: {a ** b}')
    elif symbol == ('!' or '@' or '#'):
        print(f'Please enter a valid symbol.')
    else:
        print('Something went wrong. Please check your input.')

# examples
# Multiplication
calculate(3, 5, '*')
# Division
calculate(10, 2, '//')
# invalid symbol
calculate(20, 5, '!')
# any other input
calculate(20, 5, 'ghsd 2')

# Bonus task - define a function to calculate total years of work experience based on users input

def total_experience():
    job_1 = int(input('Please enter years of experience at job 1: '))
    job_2 = int(input('Please enter years of experience at job 2: '))
    job_3 = int(input('Please enter years of experience at job 3: '))
    work_experience = (job_1, job_2, job_3)
    total = sum(work_experience)
    print(total)

# Call function
# total_experience()