""" Write a program that generates system login names for students. You will use the following algorithm to generate a login name:
1) Get the first three characters of the student’s first name. (If the first name is less than three characters in length, use the entire first name.)
2) Get the first three characters of the student’s last name. (If the last name is less than three characters in length, use the entire last name.)
3) Get the last three characters of the student’s ID number. (If the ID number is less than three characters in length, use the entire ID number.)
Concatenate the three sets of characters to generate the login name.
For example, if a student’s name is Amanda Spencer, and her ID number is CMPT6721, her login name would be AmaSpe721. """

def main():
    first_name = input('Enter your first name: ')[0:3]
    last_name = input('Enter your last name: ')[0:3]
    id =input('Enter your id: ')[-3:]
    #id_updated = id[-3:]
    print(first_name + last_name + id)
main()


