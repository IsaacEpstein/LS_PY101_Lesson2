import json

# Open the JSON file for reading
with open('calculator_messages.json', 'r') as file:
    MESSAGES = json.load(file)

# Now 'data' contains the contents of the JSON file as a Python dictionary or list

def prompt(message):
    print(f"==> {message}")

def invalid_number(number_str):
    try:
        int(number_str)
    except ValueError:
        return True

    return False

prompt(MESSAGES['welcome'])

while True:

    prompt(MESSAGES['first_number'])
    number1 = input()

    while invalid_number(number1):
        prompt(MESSAGES['invalid_number'])
        number1 = input()

    prompt(MESSAGES['second_number'])
    number2 = input()

    while invalid_number(number2):
        prompt(MESSAGES['invalid_number'])
        number2 = input()

    prompt(MESSAGES['operation'])
    operation = input()

    while operation not in ["1", "2", "3", "4"]:
        prompt(MESSAGES['choose1234'])
        operation = input()

    match operation:
        case "1":
            output = int(number1) + int(number2)
        case "2":
            output = int(number1) - int(number2)
        case "3":
            output = int(number1) * int(number2)
        case "4":
            output = int(number1) / int(number2)

    prompt(f"{MESSAGES['result']} {output}")

    prompt(MESSAGES['another_calc'])
    again = input()
    if again and again.lower() == 'y':
        prompt(MESSAGES['go_again'])
        continue
    else:
        break