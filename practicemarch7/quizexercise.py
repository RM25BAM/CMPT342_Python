def main(): 
    solutions = ['A', 'A', 'A', 'B', 'B', 'B', 'C', 'C', 'C', 'D']
    student_solutions = getInput()

    displayResults(student_solutions, solutions)
def getInput():
    user_input = []
    for i in range(0, 10):
        # value cant go past a to d 
        user = input(f"Enter your response for question : ").upper()
        if (user.isdigit() == False) and (len(user) == 1) and user.isalpha() and (user == 'A' or user == 'B' or user == 'C' or user == 'D') :
            user_input.insert(i, user)
        else:
            while True: 
                user = input(f"Enter a valid response for question: ")
                if (user.isdigit() == False) and (len(user) == 1) and user.isalpha() and (user == 'A' or user == 'B' or user == 'C' or user == 'D') :
                    user_input.insert(i, user)
                    break

    print(user_input)
    return user_input
    #user_input = [item for item in user_input in input(f"Enter your response for question {j+1}: ")]

def displayResults(student_solutions, solutions):
    num_correct = 0
    num_wrong = 0
    incorrect = []
    print(student_solutions)
    print(solutions)
    for i in range(len(solutions)):
        for j in range(len(student_solutions)):
            if solutions[i] == student_solutions[j]:
                num_correct += 1
                continue
            else:
                num_wrong += 1
                incorrect.append(student_solutions[j])
    print( num_correct)
    print(num_wrong)
    print(incorrect)
main()