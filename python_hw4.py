""" Write a program that lets the user play the game of Rock, Paper, Scissors against the computer. The program should work as follows:

When the program begins, a random number in the range of 1 through 3 is generated. If the number is 1, then the computer has chosen rock. If the number is 2, then the computer has chosen paper. If the number is 3, then the computer has chosen scissors. (Don’t display the computer’s choice yet.)

Your program lets the user enter their choice of “rock,” “paper,” or “scissors” at the keyboard.

Then, the computer’s choice is displayed.

A winner is selected according to the following rules:

If one player chooses rock and the other player chooses scissors, then rock wins. (Rock smashes scissors.)

If one player chooses scissors and the other player chooses paper, then scissors wins. (Scissors cuts paper.)

If one player chooses paper and the other player chooses rock, then paper wins. (Paper wraps rock.)

If both players make the same choice, the game must be played again to determine the winner.

Your program will have the following functions:

getRandom – returns a randomly generated number between 1 and 3

numberToString – takes a number and returns its string equivalent (1 is rock, 2 is paper, 3 is scissors).

getInput – gets input from the user, and returns the user entered string, user may only enter the strings - rock, paper or scissors. If the user enters any other string, keep asking the user for the correct string.

stringToNumber – takes the user input string, converts it to the corresponding integer and returns the value (rock is 1, paper is 2 and scissors is 3).

main – implements the core logic and uses the above four helper functions.

Do not use any global variables or constants.

Your output should be formatted similar to the following. Note that the program runs in a loop as long as the computer and the player make the same choice. """
""" 
import random

def main():
  user_input = getInput()
  computer =getRandom() 
  user = stringToNumber(user_input.lower())
  if(user == computer):
     print('You made the same choice as the computer. Try again.')
     main()
  elif(user == 1 and computer == 2) or (user == 2 and computer == 3) or (user == 3 and computer == 1):
     user = numberToString(user)
     computer = numberToString(computer)
     print(f'Computer chose {computer}')
     print(f'You chose {user}')
     print('Computer wins the game')
  elif(user == 2 and computer == 1) or (user == 3 and computer == 2) or (user == 1 and computer == 3):
     user = numberToString(user)
     computer = numberToString(computer)
     print(f'Computer chose {computer}')
     print(f'You chose {user}')
     print('You win the game')
def getRandom():
    computer = random.choice([1, 3])
    return computer
def numberToString(num):
   if (num == 1):
      return 'rock'
   elif (num == 2):
      return 'paper'
   elif (num == 3):
      return 'scissors'
   pass
def getInput(): ##done
   result = input("Enter rock, paper or scissors:")
   return result
def stringToNumber(user_input): ##done
   if(user_input == 'rock'):
      return 1
   elif (user_input == 'paper'):
      return 2
   elif (user_input == 'scissors'):
      return 3
   else:
      main()
main()  """
