# Ask the user for the first number.
# Ask the user for the second number.
# Ask the user for the type of operation to perform
# Perform the operation on the two numbers
# Print the result

"""
Calculator program that performs basic arithmetic operations.
"""

def prompt(message):
    """Print a message with a prompt indicator."""
    print(f'===> {message}')

def invalid_number(number_str):
    """Check if a string can be converted to an integer.
    
    Returns True if invalid, False if valid.
    """
    try:
        int(number_str)
    except ValueError:
        return True
    return False

prompt('Welcome to Calculator!')
prompt('Enter the first number: ')
number1 = input()

while invalid_number(number1):
    prompt('Invalid number. Please enter an integer.')
    number1 = input()

prompt('Enter the second number: ')
number2 = input()

while invalid_number(number2):
    prompt('Invalid number. Please enter an integer.')
    number2 = input()

prompt(f'Number1 is {number1} and Number2 is {number2}.')

prompt('What operation do you want to perform? '
                 '1) add, 2) subtract, 3) multiply, or 4) divide: ')
operator = input()

while operator not in ['1', '2', '3', '4']:
    prompt('Oops. Please enter 1, 2, 3 or 4.')
    operator = input()

match operator:
    case '1':
        prompt(f'The result is {int(number1) + int(number2)}.')
    case '2':
        prompt(f'The result is {int(number1) - int(number2)}.')
    case '3':
        prompt(f'The result is {int(number1) * int(number2)}.')
    case '4':
        prompt(f'The result is {int(number1) / int(number2)}.')
