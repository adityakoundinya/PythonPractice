computerChoice = 'scissors'
userChoice = input("Whats your pick? \n");

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