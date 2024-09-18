""" ##1.       Look at the following function definition:

def my_function(a, b, c):

     d = (a + c) / b
     print(d)
def main():
    a , b, c = 2, 4, 6
    my_function(a,b,c)
main() 
###Write a statement that calls this function and uses keyword arguments to pass 2 into a, 4 into b, and 6 into c.

 

 

 ##2.       The following statement calls a function named half, which returns a value that is half that of the argument. Write the code for the function. The function call would be:



def half(number):
    number = number / 2
    return number
def main():
    number = int(input("Enter a number:"))
    result = half(number)
    print("Result = ", result)
main() 
##3.       What is wrong with the function header below:

#header shouldn't have tax = 0.08 because when it calls the function it setting tax = 0.1 it should be 10 percent of 100%
def get_salestax(tax = 0.08 , amount):

    print(tax * amount)

 

get_salestax(0.1, 100)  
## to fix it take out the 0.08
def get_salestax(tax , amount):

     print(tax * amount)

 

get_salestax(0.1, 100) 

# Function call to calculate 10% sales tax on $100

 

#4.       Write a function named get_name that asks the user to enter their first and last name in two separate statements, stores them in two separate variables and returns the two values. Following would be the function call:


def get_name():
    first = input("Enter your first name:")
    last = input("Enter your last name:")
    return first, last
first, last = get_name()
print(first,end =" ")
print(last)

 ##5.       What will the following program display?

 
The  following program displays the print value of x and y. then it calls a function change_us(x,y) then it sets inside function a and b both equal to 0 and prints a and b.
then it print the original x and y from main function. only changes in the function not in main
def main():

     x = 1

     y = 3.4

     print(x, y)

     change_us(x, y)

     print(x, y)

    

def change_us(a, b):

     a = 0

     b = 0

     print(a, b)

 

main() 
 """