import random
def main():

    # Initialize dictionary with 10 countries

    capitals = {'UAE':'Abu Dhabi', 'Yemen':'Sanaa',

                'Cayman Islands':'George Town', 'Vietnam':'Hanoi',

                'Nepal':'Kathmandu', 'Afghanistan':'Kabul',

                'Rwanda':'Kigali', 'Myanmar':'Naypyidaw',

                'Greenland':'Nuuk', 'Namibia':'Windhoek'}                



    # Randomly select 5 countries and store in a list

    random_list = random.sample(list(capitals.keys()), 5)



    # Local variable to hold number of correct answers

    correct = 0

    

    for i in random_list:

        user_solution = input(f'What is the capital of {i}? ')        

        # User solution is correct.

        if user_solution == capitals[i]:

            correct = correct + 1

            print('That is correct.')

        # User solution is incorrect.

        else:

            print('That is incorrect.')

            print(f'The correct answer is {capitals[i]}')



    print(f'\nYou correctly answered {correct} questions.')        

main()
