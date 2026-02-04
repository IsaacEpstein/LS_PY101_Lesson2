import json

# Load messages once when program starts
with open('calculator_messages.json', 'r') as file:
    MESSAGES = json.load(file)

def invalid_number(number_str):
    """Check if a string can be converted to a valid number."""
    try:
        float(number_str)
    except ValueError:
        return True
    return False

def messages(message, lang):
    """Retrieve a message from MESSAGES dictionary."""
    return MESSAGES[lang][message]

def prompt(key, lang):
    """Display a formatted message to the user."""
    message = messages(key, lang)
    print(f"==> {message}")

def select_language():
    """Prompt user to select a language and return language code."""
    print("Select your language / 选择你的语言:")
    print("1. English")
    print("2. Chinese (中文)")
    
    choice = input().strip().lower()
    
    # Accept multiple variations
    if choice in ['1', 'english', 'en', 'e']:
        return "en"
    elif choice in ['2', 'chinese', 'zh', 'c', '中文']:
        return "zh"
    else:
        # Default to English if invalid input
        print("Defaulting to English...")
        return "en"

def get_number(prompt_key, lang):
    """Get a valid number from user with validation loop."""
    prompt(prompt_key, lang)
    number = input().strip()
    
    while invalid_number(number):
        prompt('invalid_number', lang)
        number = input().strip()
    
    return float(number)

def get_operation(lang):
    """Get a valid operation choice from user."""
    prompt('operation', lang)
    operation = input().strip()
    
    while operation not in ["1", "2", "3", "4"]:
        prompt('choose1234', lang)
        operation = input().strip()
    
    return operation

def calculate(num1, num2, operation):
    """Perform calculation based on operation choice."""
    match operation:
        case "1":
            return num1 + num2
        case "2":
            return num1 - num2
        case "3":
            return num1 * num2
        case "4":
            if num2 == 0:
                return None  # Signal division by zero
            return num1 / num2

def display_result(num1, num2, operation, result, lang):
    """Display the calculation result in a formatted way."""
    operations_symbols = {
        "1": "+",
        "2": "-",
        "3": "*",
        "4": "/"
    }
    
    symbol = operations_symbols[operation]
    result_msg = messages('result', lang)
    print(f"==> {num1} {symbol} {num2} = {result:.2f}")

def play_again(lang):
    """Ask user if they want to perform another calculation."""
    prompt('another_calc', lang)
    again = input().strip().lower()
    
    if again and again[0] == 'y':
        return True
    return False

def main():
    """Main calculator program."""
    lang = select_language()
    prompt('welcome', lang)
    
    while True:
        # Get numbers
        number1 = get_number('first_number', lang)
        number2 = get_number('second_number', lang)
        
        # Get operation
        operation = get_operation(lang)
        
        # Calculate
        result = calculate(number1, number2, operation)
        
        # Handle division by zero
        if result is None:
            if lang == "en":
                print("==> Error: Cannot divide by zero!")
            else:
                print("==> 错误：不能除以零！")
            continue
        
        # Display result
        display_result(number1, number2, operation, result, lang)
        
        # Check if user wants to continue
        if not play_again(lang):
            break
        
        prompt('go_again', lang)

# Run the program
main()