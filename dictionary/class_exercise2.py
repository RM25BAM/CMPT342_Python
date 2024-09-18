#program that lets user enter a course number and then display the course room number instructor and meeting time
def main():
    rooms = {
        'CS101' : 3004,
        'CS102' : 4501,
        'CS103' : 6755
    }
    instructors = {
        'CS101' : 'Dr.T',
        'CS102' : 'Dr.K',
        'CS103' : 'Dr.A'
    }
    times = {
        'CS101' : '8:00 am',
        'CS102' : '9:00 am',
        'CS103' : '10:00 am'
    }
    while True:
        option = int(input('Option 1: see class info, Option 2: Change instructor'))
        if option == 1:
            Course_input = input('Enter your course number: ')
            for i in rooms.items():
                if Course_input not in rooms:
                    print(f'{Course_input} Not valid input')
                else:
                    break
            print(f'The details of course room is : {rooms[Course_input]}')
            print(f'The details of course instructor is : {instructors[Course_input]}')
            print(f'The details of course time is : {times[Course_input]}')
            continue_run = input('Would you like to continue y/n?')
            if continue_run == 'y':
                continue
            elif continue_run == 'n':
                break
        elif option == 2:
            user_input = input('Enter the course number: ')
            for i in rooms.items():
                print(rooms.items())
                if user_input not in rooms:
                    print(f'{user_input} Not valid input')
                else:
                    break
            new_instructor = input('Enter the new instructor: ')
            instructors[user_input] = new_instructor
            print(instructors[user_input])
        
main()

