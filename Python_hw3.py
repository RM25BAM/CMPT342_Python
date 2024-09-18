

""" def sum_and_average():
    sum_numbers = 0
    count = 0
    
    
    sum_numbers += number
    count += 1
    
    if count == 0:
        print("No values other than a 0 were entered")
    else:
        average = sum_numbers / count
        print(f"Total = {sum_numbers:.2f}")
        print(f"Average = {average:.2f}")

 

#QUESTION 1
value = []
user_in = float(input("Enter a number (0 to quit): "))
while user_in != 0:
    ###total += total + number
    update_in = float(input("Enter a number (0 to quit): "))
    value.append(user_in)
    user_in = update_in
length = len(value) 
sum = sum(value)
avg = sum / length
print("Total =", end =" ")         
print("%.2f" % sum)             
print("Average =", end =" "), 
print("%.2f" % avg)    


#To run the function, simply call it:
sum_and_average()




def main():
    product = 1
    user_in = int(input("Enter a nonnegative integer:"))
    if user_in <= 0:
        main()
    else: 
        for i in range (1, user_in+1): 
            product *= i
        print(f"The factorial of {user_in} is", end = " ")
        print(f"{product:,d}")
main()  """ 