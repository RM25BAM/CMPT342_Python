import random

# The Coin class simulates a coin that can be flipped.
class Coin:

    def __init__(self):
        self.__sideup = 'Heads'

    def toss(self):
        if random.randint(0, 1) == 0:
            self.__sideup = 'Heads'
        else:
            self.__sideup = 'Tails'

    def get_sideup(self):
        return self.__sideup

# The main function.
def main():
    # Create an object from the Coin class.
    my_coin = Coin()

    # Toss the coin 10 times.
    print('I am going to toss the coin ten times:')
    for count in range(10):
        my_coin.toss()
        print(my_coin.get_sideup())

# Call the main function.
if __name__ == '__main__':
      main()