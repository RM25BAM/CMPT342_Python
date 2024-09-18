""" import random
numbers = [0] * 5 # Creates [0, 0, 0, 0, 0]
for i in range(len(numbers)):
    numbers[i] = random.randint(0, 9)
print(numbers) """
""" numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers[1:8:2])
print(numbers[-5:]) """
""" student_id = [101, 102, 103, 104]
student_id.append(105)
print(student_id.index(103))
student_id.insert(2, 1010)
print(student_id) """
""" numbers = [3, 1, 2, 4]
print(sum(numbers))
print(max(numbers))
print(min(numbers)) """
""" def main():
    numbers = [2, 1, 5, 4]
    print(get_total(numbers))
    numbers = get_values()    
    print(numbers)
def get_total(value_list):
    total= 0
    for i in value_list:
        total += i

    return total

def get_values():
    values = []
    for i in range(5):
        num = int(input('Enter a number: '))
        values.append(num)
    return values
main()"""
""" 
def main():
    # Create a list of strings.
    cities = ['New York', 'Kathmandu', 'Addis Ababa', 'Havana']

    # Write the list to a file.
    with open('cities.txt', 'w') as outfile:
        outfile.writelines(cities)

# Call the main function.
if __name__ == '__main__':
    main()

# This program saves a list of strings to a file.

def main():
    # Create a list of strings.
    cities = ['New York', 'Kathmandu', 'Addis Ababa', 'Havana']

    # Write the list to a file.
    with open('cities.txt', 'w') as outfile:
        for item in cities:
            outfile.write(item + '\n')

# Call the main function.
if __name__ == '__main__':
    main()

def main():
    # Read the contents of the file into a list.
    with open('cities.txt', 'r') as infile:
        cities = infile.readlines()
        print(cities) # ['New York\n', 'Kathmandu\n', 'Addis Ababa\n', 'Havana\n']
    
    # Strip the \n from each element.
    for index in range(len(cities)):
        cities[index] = cities[index].rstrip('\n')

    # Print the contents of the list.
    print(cities) # ['New York', 'Kathmandu', 'Addis Ababa', 'Havana']

# Call the main function.
if __name__ == '__main__':
    main()
 """
def main():
    # Create a list of strings.
    scores = [85, 75, 95, 100, 45]

    # Write the list to a file.
    with open('scores.txt', 'w') as outfile:
        for item in scores:
            outfile.write(str(item) + '\n')

def main():
    # Read the contents of the file into a list.
    with open('scores.txt', 'r') as infile:
        scores = infile.readlines()
       
    # Strip the \n from each element.
    for index in range(len(scores)):
        scores[index] = int(scores[index].rstrip('\n'))

    # Print the contents of the list.
    print(scores) # [85, 75, 95, 100, 45]

# Call the main function.
if __name__ == '__main__':
    main()