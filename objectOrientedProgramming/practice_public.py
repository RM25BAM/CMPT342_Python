import random

# The Coin class simulates a coin that can be flipped.
class Coin:
   # _ _sideup makes it a private variable and .sideup makes it public
    def __init__(self):
        self.sideup = 'Heads' #sideup is public 
    
    def toss(self):
        if random.randint(0, 1) == 0:
            self.sideup = 'Heads'
        else:
            self.sideup = 'Tails'
    
    def get_sideup(self):
        return self.sideup

# The main function.
def main():
    # Create an object from the Coin class.
    my_coin = Coin()

    # Toss the coin.
    print('I am tossing the coin...')
    my_coin.toss()

    # Display the side of the coin that is facing up.
    print('This side is up:', my_coin.get_sideup())
        
# Call the main function.
if __name__ == '__main__':
      main()