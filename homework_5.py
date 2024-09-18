def main():
    try:
        user = int(input('How many student records do you want to create?'))
        for x in range (0, user):
            print(f'\nEnter data for student #{x+1}')
            Id_num =  input('ID number: ')
            Name =  input('Name: ')
            Dept = input('Dept: ')
            Midterm = int(input('Midterm score: '))
            Final = int(input('Final score: '))
            Avg = (Midterm + Final)/2
            if (Avg > 100) or (Avg < 0):
                Avg = Avgvalue()
            else:
                Record = f"{Id_num}\n{Name}\n{Dept}\n{Midterm}\n{Final}\n{Avg}"
                with open('students.txt', 'a') as f:
                    f.write(Record)
            
        print("Student record written to students.txt") 
    except ZeroDivisionError:
        print('Error: Please enter a non zero value for denominator.')
        main()
    except ValueError:
        print('Error: Please enter an integer value.') 
        main()
    except FileNotFoundError:
        print('An error in finding the file.') 
        main()
    except:
        print('An error occured.')
        main()
main()  
def Avgvalue():
    Midterm = int(input('Midterm score: '))
    Final = int(input('Final score: '))
    Avg = (Midterm + Final)/2
    if Avg > 100 or Avg < 0:
        Avg()
    return Avg
""" 
with open ('students.txt', 'r') as f:
        read = f.read()
        read = read.split("\n")
        n = len(read)
        for x in range(0, n, 3):
            if x + 2 < n:
                print(f'ID number: {read[x]}\nName: {read[x+1]}\nDept: {read[x+2]}\n')
            else:
                 break
        print('Student record from students.txt')
f.close()  """ 
