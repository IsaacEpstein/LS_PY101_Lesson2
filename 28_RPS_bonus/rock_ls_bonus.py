'''
Docstring for rock_ls_bonus.
Rock paper scissors lizard spock game 
'''

import random

VALID_CHOICES = ["rock", "paper", "scissors", "lizard", "spock"]

def prompt(message):
    '''Adds ==> to distinguish prompts from user inputs'''
    print(f"==> {message}")


def display_winner(player, computer):
    '''Displays who the winner is'''
    prompt(f"You chose {player}, computer chose {computer}")
    if ((player == "rock" and (computer == "scissors" or computer == "lizard")) or
        (player == "paper" and (computer == "rock" or computer == "spock")) or
        (player == "scissors" and (computer == "paper" or computer == "lizard")) or
        (player == "lizard" and (computer == "spock" or computer == "paper")) or
        (player == "spock" and (computer == "scissors" or computer == "rock"))):
        prompt("You win!")
        return 'player'
    if ((computer == "rock" and (player == "scissors" or player == "lizard")) or
        (computer == "paper" and (player == "rock" or player == "spock")) or
        (computer == "scissors" and (player == "paper" or player == "lizard")) or
        (computer == "lizard" and (player == "spock" or player == "paper")) or
        (computer == "spock" and (player == "scissors" or player == "rock"))):
        prompt("Computer wins!")
        return 'computer'
    prompt("It's a tie!")
    return 'tie'

def convert_choice(selection):
    '''If the user only puts in the first letter of their choice, this will convert it
to the full word.'''
    if selection == 'r':
        return 'rock'
    if selection == 'p':
        return 'paper'
    if selection == 'l':
        return 'lizard'
    if selection == 's':
        prompt("scissors or spock?")
        return input().lower().strip()
    return selection

def play_again():
    '''this is the main program and it keeps the score as well. best of 5.'''
    score_player = 0
    score_computer = 0
    while score_player < 3 and score_computer < 3:
        prompt(f'Choose one: {", ".join(VALID_CHOICES)}')
        choice = convert_choice(input().lower().strip())

        while choice not in VALID_CHOICES:
            prompt(f"That's not a valid choice. Choose one: {', '.join(VALID_CHOICES)} ")
            choice = convert_choice(input().lower().strip())

        computer_choice = random.choice(VALID_CHOICES)

        round_winner = display_winner(choice, computer_choice)
        if round_winner == 'player':
            score_player += 1
        elif round_winner == 'computer':
            score_computer += 1
        prompt(f"You currently have {score_player} and the computer has {score_computer}.")
    if score_player == 3:
        prompt("You're the grand winner.")
    else:
        prompt("The computer is the grand winner.")

    while True:
        prompt("Do you want to play again (y/n)?")
        answer = input().lower().strip()

        if answer.startswith('n') or answer.startswith('y'):
            break
        prompt("That's not a valid choice")

    if answer.startswith('y'):
        play_again()

play_again()


'''
this is from claude.  using a dictionary for determine who wins. much better

import random

VALID_CHOICES = ["rock", "paper", "scissors", "lizard", "spock"]

WINS = {
    "rock": ("scissors", "lizard"),
    "paper": ("rock", "spock"),
    "scissors": ("paper", "lizard"),
    "lizard": ("spock", "paper"),
    "spock": ("scissors", "rock")
}

def prompt(message):
    '''Adds ==> to distinguish prompts from user inputs'''
    print(f"==> {message}")

def display_winner(player, computer):
    '''Displays who the winner is using a dictionary of winning combinations'''
    prompt(f"You chose {player}, computer chose {computer}")
    if computer in WINS[player]:
        prompt("You win!")
        return 'player'
    if player in WINS[computer]:
        prompt("Computer wins!")
        return 'computer'
    prompt("It's a tie!")
    return 'tie'

def convert_choice(selection):
    '''If the user only puts in the first letter of their choice, this will convert it
    to the full word.'''
    if selection == 'r':
        return 'rock'
    if selection == 'p':
        return 'paper'
    if selection == 'l':
        return 'lizard'
    if selection == 's':
        prompt("scissors or spock?")
        return input()
    return selection

def play_again():
    '''Main game loop, keeps score. Best of 5 rounds.'''
    score_player = 0
    score_computer = 0
    while score_player < 3 and score_computer < 3:
        prompt(f'Choose one: {", ".join(VALID_CHOICES)}')
        choice = convert_choice(input())

        while choice not in VALID_CHOICES:
            prompt(f"That's not a valid choice. Choose one: {', '.join(VALID_CHOICES)}")
            choice = convert_choice(input())

        computer_choice = random.choice(VALID_CHOICES)

        round_winner = display_winner(choice, computer_choice)
        if round_winner == 'player':
            score_player += 1
        elif round_winner == 'computer':
            score_computer += 1
        prompt(f"You currently have {score_player} and the computer has {score_computer}.")

    if score_player == 3:
        prompt("You're the grand winner.")
    else:
        prompt("The computer is the grand winner.")

    while True:
        prompt("Do you want to play again (y/n)?")
        answer = input().lower()
        if answer.startswith('n') or answer.startswith('y'):
            break
        prompt("That's not a valid choice")

    if answer.startswith('y'):
        play_again()

play_again()
'''