# The CellPhone class holds data about a cell phone.
class CellPhone:

    # The __init__ method initializes the attributes.    
    def __init__(self, manufact, model, price):
        self.__manufact = manufact
        self.__model = model
        self.__retail_price = price

    # The set_manufact method accepts an argument for
    # the phone's manufacturer.
    def set_manufact(self, manufact):
        self.__manufact = manufact

    # The set_model method accepts an argument for
    # the phone's model number.
    def set_model(self, model):
        self.__model = model

    # The set_retail_price method accepts an argument
    # for the phone's retail price.
    def set_retail_price(self, price):
        self.__retail_price = price

    # The get_manufact method returns the
    # phone's manufacturer.
    def get_manufact(self):
        return self.__manufact

    # The get_model method returns the
    # phone's model number.
    def get_model(self):
        return self.__model

    # The get_retail_price method returns the
    # phone's retail price.
    def get_retail_price(self):
        return self.__retail_price
def main():
    phones = make_list()
    print('Here is the data you entered: ')
    display_list(phones)
def make_list():
    print('Enter the data of 3 phones.')
    for i in range(1,4):
        print(f'Phone Number {i}')
        manufacturer = input('Enter the manufacturer:')
        model = input('Enter the model number:')
        price = input('Enter the retail price:')
        set_manufact(self, manufacturer)

def display_list():
    print('Heres the data you entered')