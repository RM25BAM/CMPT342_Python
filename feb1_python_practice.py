""" def main():
    quotient = divide(2,0)
    if quotient is None:
        print('Cannot divide by zero')
    else:
        print(quotient)
def divide(num1,num2):
    if num2 == 0:
        # result = None
        return
    else:
        result = num1 / num2
    return result

main() """