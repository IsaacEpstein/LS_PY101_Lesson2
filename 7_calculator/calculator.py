# Ask the user for the first number.
# Ask the user for the second number.
# Ask the user for the type of operation to perform
# Perform the operation on the two numbers
# Print the result

print('Welcome to Calculator!')
number1 = input('Enter the first number: ')
number2 = input('Enter the second number: ')
print(f'Number1 is {number1} and Number2 is {number2}.')
operator = input('What operation do you want to perform? '
                 '1) add, 2) subtract, 3) multiply, or 4) divide: ')
if operator == '1':
    print(f'The result is {int(number1) + int(number2)}.')
elif operator == '2':
    print(f'The result is {int(number1) - int(number2)}.')
elif operator == '3':
    print(f'The result is {int(number1) * int(number2)}.')
elif operator == '4':
    print(f'The result is {int(number1) / int(number2)}.')
else:
    print('Invalid input.')

