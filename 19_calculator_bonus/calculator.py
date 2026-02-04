import json

# Open the JSON file for reading
with open('calculator_messages.json', 'r') as file:
    MESSAGES = json.load(file)

# Now 'data' contains the contents of the JSON file as a Python dictionary or list

# def prompt(message):
#     print(f"==> {message}")

def invalid_number(number_str):
    try:
        float(number_str)
    except ValueError:
        return True

    return False

print("Which language is better, English or Chinese? ")
language_code = ""
language = input()
if language == 'English':
    language_code = "en"
else:
    language_code = "zh"

def messages(message, language_code):
    return MESSAGES[language_code][message]

def prompt(key, language_code):
    message = messages(key, language_code)
    print(f"==> {message}")

prompt('welcome', language_code)

while True:

    prompt('first_number')
    number1 = input()

    while invalid_number(number1):
        prompt('invalid_number')
        number1 = input()

    prompt('second_number')
    number2 = input()

    while invalid_number(number2):
        prompt('invalid_number')
        number2 = input()

    prompt('operation')
    operation = input()

    while operation not in ["1", "2", "3", "4"]:
        prompt('choose1234')
        operation = input()

    match operation:
        case "1":
            output = float(number1) + float(number2)
        case "2":
            output = float(number1) - float(number2)
        case "3":
            output = float(number1) * float(number2)
        case "4":
            output = float(number1) / float(number2)

    print(f"{MESSAGES[language_code]['result']} {output}")


    prompt('another_calc')
    again = input()
    if again and again.lower() == 'y':
        prompt('go_again')
        continue
    else:
        break