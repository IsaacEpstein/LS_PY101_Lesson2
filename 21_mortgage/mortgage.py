'''
Docstring for mortgage.py
A mortgage calculator for car payments which determines
the monthly payment 

-Inputs:
the loan amount (float)
monthly interest rate (float)
loan duration (float - months)

-Output: 
monthly payment (float)

-requirements:
all numbers must be positive
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
def prompt(message):
    print(f'===> {message}')

def monthly_payment(loan, monthly_rate, monthly_term):
    if monthly_rate == 0:
        return loan / monthly_term
    return (loan * (monthly_rate / (1 - (1 + monthly_rate) ** (-monthly_term))))

def check_entry(message):
    while True:
        try:
            clean = message.replace("$", "").replace(",", "").strip()
            number = float(clean)

            if number < 0:
                prompt("Can't enter a negative number. Please enter again")
                message = input()
            else:
                return number
        except ValueError:
            prompt(f"{message} is not valid. Please enter again.")
            message = input()

def main():
    prompt('What is the total loan amount? ')
    loan_amount = check_entry(input())
    prompt("what is the annual interest rate? ")
    annual_rate = check_entry(input())
    prompt("What is the term of the loan in years? ")
    yearly_term = check_entry(input())
    monthly_amount = monthly_payment(loan_amount, annual_rate / 100 / 12, yearly_term * 12)
    prompt(f"The monthly payment is ${monthly_amount:.2f}.")

main()
