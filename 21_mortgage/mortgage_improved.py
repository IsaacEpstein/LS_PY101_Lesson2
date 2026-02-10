'''
Docstring for mortgage.py
A mortgage calculator which determines the monthly payment 

-Inputs:
the loan amount (float)
monthly interest rate (float)
loan duration (float - months)

-Output: 
monthly payment (float)

-requirements:
all numbers must be positive and non-zero
annual interest rate needs to be converted into a montly rate

Loan: $100,000
Loan duration: 10 years
Annual Interest rate: 6%
Monthly Payment: $1,110.21

Define a function which calculates and returns the monthly payment
Define a main function in which:
    Ask the user for the loan amount
    Ask the user for the annual interest rate
    Ask the user for the term of the loan in years
    Save those values to variables
    call the function which calculates and returns the monthly payment
    Print out the dollar amount for the monthly payment using $ and two decimals.
Call the main function
'''

MONTHS_IN_YEAR = 12

def prompt(message):
    print(f'===> {message}')

def monthly_payment(loan, monthly_rate, monthly_term):
    if monthly_rate == 0:
        return loan / monthly_term
    return (loan * (monthly_rate / (1 - (1 + monthly_rate) ** (-monthly_term))))

def check_entry(message, allow_zero=False):
    while True:
        try:
            cleaned_input = message.replace("$", "").replace(",", "").strip()
            number = float(cleaned_input)

            if number < 0:
                prompt("Can't enter a negative number. Please enter again")
                message = input()
            elif number == 0 and not allow_zero:
                prompt("Can't enter zero. Please enter again")
                message = input()
            else:
                return number
        except ValueError:
            prompt(f"{message} is not valid. Please enter again.")
            message = input()

def get_loan_amount():
    prompt('What is the total loan amount?')
    return check_entry(input())

def get_annual_rate():
    prompt('What is the annual interest rate?')
    return check_entry(input(), allow_zero=True)

def get_loan_term():
    prompt('What is the term of the loan in years?')
    return check_entry(input())

def main():
    loan_amount = get_loan_amount()
    annual_rate = get_annual_rate()
    yearly_term = get_loan_term()
    
    prompt("Loan Details:")
    prompt(f"- Loan Amount: ${loan_amount:,.2f}")
    prompt(f"- Annual Interest Rate: {annual_rate}%")
    prompt(f"- Loan Term: {yearly_term} years")
    print()
    
    monthly_amount = monthly_payment(loan_amount, 
                                    annual_rate / 100 / MONTHS_IN_YEAR, 
                                    yearly_term * MONTHS_IN_YEAR)
    prompt(f"Your monthly payment is: ${monthly_amount:,.2f}")

main()