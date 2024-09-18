import pickle
def main():
    students = dict()
    choice = 0
    while choice != 5:
        print()
        print('Menu')
        print('---------------------------------')
        print('1. Look up a name')
        print('2. Add a new ID and name')
        print('3. Change an existing name')
        print('4. Delete an ID and name')
        print('5. Quit the program')
        print()
        choice = int(input('Enter your choice: '))
        
        while choice < 1 or choice > 5:
            choice = int(input('Please enter a valid choice: '))
        if choice == 1:
            lookup(students)
        elif choice == 2:
            add(students)
        elif choice == 3:
            change(students)
        elif choice == 4:
            delete(students)
        else:
            break
def lookup(students):
    pass
def add(students):
    pass
def change(students):
    pass
def delete(students):
    pass
main()