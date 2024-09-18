
""" import math  
def main():
    output = 0.01
    user_sal = []
    user = int(input('Enter the number of days:')) 
    if user == 0:
        print("Employee can't work zero days. Try again!")
        main()
    for x in range(0,user):
        if(x==0): 
            user_sal.append(output)
        else:
            output *= 2 
            user_sal.append(output)
    print_table(user_sal,user) 
    #for x in range(0, len(user_sal)):
    Sum = sum(user_sal)
    print(f'The total salary for {user} days is: ${Sum:.2f}')
def print_table(user_sal,user): 
    num = 0
    iter = -1
    print('Day',end='     ') 
    print('Salary') 
    print('-------------------------') 
    for x in range (0,user):
        num += 1
        iter += 1 
        print(f'{num}',end='     ') 
        print(f'${user_sal[iter]}')
main()
 """
""" def main():
    output = 0.01
    user_sal = []
    user = int(input('Enter the number of days:')) 
    if user == 0:
        print("Employee can't work zero days. Try again!")
        main()
    for x in range(0,user):
            if(x==0): 
                user_sal.append(output)
            else:
                output *= 2 
                user_sal.append(output)
    print('Day',end='     ') 
    print('Salary') 
    print('-------------------------') 
    num, iter = 0, -1
    for x in range(0,len(user_sal)):
       num += 1
       iter += 1
       print(f'{num}',end='     ') 
       print(f'${user_sal[iter]}')
    Sum = sum(user_sal)
    print(f'The total salary for {user} days is: ${Sum:.2f}')
main() """
""" def main():
    output = 0.01
    user = int(input('Enter the number of days:'))
    if user == 0:
        print("Employee can't work zero days. Try again!")
        main()
    print('Day',end='     ') 
    print('Salary') 
    print('-------------------------') 
    num, Sum = 0, 0
    for x in range(0,user):
        num += 1
        print(f'{num}',end='     ') 
        print(f'${output}')
        Sum += output
        output *= 2
    print(f'The total salary for {user} days is: ${Sum:.2f}')
main() """