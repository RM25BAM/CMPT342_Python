""" # This program divides a number by another number.

def main():
    try:        
        num1 = int(input('Enter a number: '))
        num2 = int(input('Enter another number: '))
        result = num1 / num2
        print(f'{num1} divided by {num2} is {result}')
    except ValueError:
        print('Error: Please enter a numeric value.')

            
# Call the main function.
 if __name__ == '__main__': 
main() """
# This program displays the total of the
# amounts in the sales_data.txt file.
""" 
def main():
    # Initialize an accumulator.
    total = 0.0
    
    try:
        # Open the sales_data.txt file.
        with open('/Users/npiedrabuena/Desktop/Python class/exercises/sales_data.txt', 'r') as infile:
            # Read the values from the file and accumulate them.
            for line in infile:
                amount = float(line)
                total += amount

        # Print the total.
        print(f'{total:,.2f}')
        
    except FileNotFoundError:
        print('An error occurred trying to read the file.')

    except ValueError:
        print('Non-numeric data found in the file.')

    except:
        print('An error occurred.')

# Call the main function.
if __name__ == '__main__':
    main() """