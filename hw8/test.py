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
        print('6. read dat file')
        print()
        choice = int(input('Enter your choice: '))
        
        while choice < 1 or choice > 6:
            choice = int(input('Please enter a valid choice: '))
        if choice == 1:
            lookup(students)
        elif choice == 2:
            add(students)
        elif choice == 3:
            change(students)
        elif choice == 4:
            delete(students)
        elif choice == 5:
            with open('/Users/natashapiedrabuena/Desktop/Python class/hw8/students.dat','wb') as output_file:
                pickle.dump(students, output_file)
            break
        elif choice == 6:  
            read(students)
     

def lookup(students):
    student_id = input("Enter ID: ")
    if student_id in students:
        print(f"Name: {students[student_id]}")
    else:
        print("The specified ID was not found.")

def add(students):
    student_id = input("Enter ID: ")
    name = input("Enter the student name: ")
    
    if student_id in students:
        print("Thst ID already exists.")
    else:
        students[student_id] = name
        print("ID and name have been added.")

def change(students):
    student_id = input("Enter ID: ")
    if student_id in students:
        new_name = input("Enter the new name: ")
        students[student_id] = new_name
        print("Information updated.")
    else:
        print("The specified ID was not found.")

def delete(students):
    student_id = input("Enter ID: ")
    if student_id in students:
        del students[student_id]
        print("Information deleted.")
    else:
        print("The specified ID was not found.")
def read(students):
    try:
        with open('/Users/natashapiedrabuena/Desktop/Python class/hw8/students.dat','rb') as input_file:
            studentsfile = pickle.load(input_file)
            print('Students Info')
            print('---------------------------------')
            for student_id, name in studentsfile.items():
                print(f"ID: {student_id}     Name: {name}")
    except FileNotFoundError: 
        print('File not created/ File not found. ')
main()

