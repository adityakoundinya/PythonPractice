import random

isExit = 1

while(True):
    choices = {
        "r": "rock",
        "p": "paper",
        "s": "scissors"
    }
    computerChoice = random.choice(list(choices.values()))
    uC = input("Whats your pick (r, p or s)? (Enter e to quit)\n")
    if uC == "e":
        break
    userChoice = choices[uC]
    if(computerChoice == userChoice):
        print("Tie")
    elif userChoice == 'paper' and computerChoice == 'rock':
        print("win")
    elif userChoice == 'scissors' and computerChoice == 'paper':
        print("win")
    elif userChoice == 'rock' and computerChoice == 'scissors':
        print("win")
    else:
        print("Lose")
    print("You chose " + userChoice + " computer chose " + computerChoice)
