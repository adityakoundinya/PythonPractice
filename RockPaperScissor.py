import random

isExit = 1;

while(isExit == 1):
  choices = ["rock", "paper", "scissors"];
  computerChoice = random.choice(choices);
  userChoice = input("Whats your pick? \n");
  if userChoice == 'exit':
    isExit = 0;
    break;
  if(computerChoice == userChoice):
    print("Tie");
  elif userChoice == 'paper' and computerChoice == 'rock':
    print("win");
  elif userChoice == 'scissors' and computerChoice == 'paper':
    print("win");
  elif userChoice == 'rock' and computerChoice == 'scissors':
    print("win");
  else:
    print("Lose");
  print("You chose " + userChoice + " computer chose " + computerChoice);
