'''
Docstring for rock
Make a rock paper scissor game where the user makes a choice
the computer makes a choice and then the winner is displayed

inputs: the user inputs a choice, rock, paper or scissors
requirements: the program randomly picks one of the three
output: print who is the winner

example
===> Please enter rock, paper or scissors (r, p, or s)?
r
===> The computer has picked scissors.
===> Rock beats scissors.  You're the winner!
===> Do you want to play again?

Input: string 
Output: string

The program prompts the user to pick rock paper or scissors.
The user enters their choice and the program saves that choice.
The program randomly selects one of the three.
The program then compares the user's choice and its own choice.
The program decides who wins or if it's a draw.
The program prints who picked what and who is the winner.
The program asks if the user wants to play again, yes or no (y/n).

We need functions to:
1. ask the user for their selection and save that value
2. compare the choices and pick the winner
3. print who won
4. ask the user if they want to play again.
'''
import random

def prompt(message):
    print(f"===> {message}")

def user_pick():
    while True:
        prompt('Rock, paper, scissor (r, p, s)? ')
        choice = input().lower().strip()

        if choice in ['r', 'rock']:
            return 'rock'
        elif choice in ['p', 'paper']:
            return 'paper'
        elif choice in ['s', 'scissors']:
            return 'scissors'
        else:
            if invalid_entry():
                continue
            else:
                return None

def invalid_entry():
    prompt("Invalid entry. Do you want to try again? (y/n) ")
    while True:
        again = input().lower().strip()
        if again == 'y':
            return True
        elif again == 'n':
            return False 
        else:
            prompt("Please only enter 'y' or 'n'.")
        
def user_wins(user, computer):
    prompt(f"Your {user} beats the computer's {computer}.")

def computer_wins(user, computer):
        prompt(f"Your {user} loses to the computer's {computer}.")

def tie(user):
    prompt(f"You and the computer both picked {user}. It's a draw.")

def compare_user_computer(user_choice, computer_choice):
    if ((user_choice == 'rock' and computer_choice == 'paper') or
       (user_choice == 'paper' and computer_choice == 'scissors') or
       (user_choice == 'scissors' and computer_choice == 'rock')):
       computer_wins(user_choice, computer_choice)
    elif  ((user_choice == 'paper' and computer_choice == 'rock') or
       (user_choice == 'scissors' and computer_choice == 'paper') or
       (user_choice == 'rock' and computer_choice == 'scissors')):
       user_wins(user_choice, computer_choice)
    else:
        tie(user_choice)

def play_again():
    prompt("Do you want to play again (y/n)? ")
    while True:
        again = input().lower().strip()
        if again == 'y':
            return True
        elif again == 'n':
            return False
        else:
            prompt("Please only enter 'y' or 'n'")
                   
def main():
    while True:
        user_choice = user_pick()
        if user_choice is None:
            break
        computer_choice = random.choice(['rock', 'paper', 'scissors'])
        compare_user_computer(user_choice, computer_choice)
        if not play_again():
            break

main()

