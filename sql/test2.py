import sqlite3

def main():
    # Connect to the database.
    conn = sqlite3.connect('test.db')
    
    # Get a cursor.
    cur = conn.cursor()

    cur.execute("DROP TABLE IF EXISTS Student")
    
    # Create the table, if it doesn't already exist.
    cur.execute('''CREATE TABLE IF NOT EXISTS Student (StudentID INTEGER NOT NULL,
                                                      StudentName TEXT,
                                                      StudentDept TEXT,
                                                      PRIMARY KEY (StudentID))''')
    
    # cur.execute("DELETE FROM Student")

    # Add a row to the table.
    cur.execute('''INSERT INTO Student (StudentID, StudentName, StudentDept)
                   VALUES (1, "Jane Doe", "CS")''')
    
    # Add another row to the table.
    cur.execute('''INSERT INTO Student
                   VALUES (2, "John Doe", "BIO")''')

    print('Current Student Information')
    
    # Select data from the table.
    cur.execute('SELECT * FROM Student')

    # Fetch the results of the SELECT statement.
    results = cur.fetchall()
    
    # Print the header for the output.
    print(f"{'StudentID':15} {'StudentName':15} {'StudentDept':15}")
    
    # Display the results. Numbers are right aligned by default.
    # Use the < operator to left align the numbers.
    for row in results:
        print(f'{row[0]:<15} {row[1]:15} {row[2]:15}')

    # Get the student ID whose dept needs to be changed    
    sid = int(input('\nEnter Student ID to change their deptartment: '))
    cur.execute('SELECT StudentDept FROM Student WHERE StudentID = ?', (sid,))
    row = cur.fetchone()

    # Check if the student id exists in the database
    if not row: # Empty lists are false
      print('No student found in the database')
    else:    
        print('The current department is:', row[0])
        sDept = input('Enter the new department: ')
        cur.execute('''UPDATE Student
                    SET StudentDept = ?
                    WHERE StudentID == ?''',
                    (sDept, sid))

        print('\nDatabase Updated.')
        print('Updated Student Information')
        
        # Select data from the table.
        cur.execute('SELECT * FROM Student')

        # Fetch the results of the SELECT statement.
        results = cur.fetchall()
        
        # Print the header for the output.
        print(f"{'StudentID':15} {'StudentName':15} {'StudentDept':15}")
        
        # Display the results. Numbers are right aligned by default.
        # Use the < operator to left align the numbers.
        for row in results:
            print(f'{row[0]:<15} {row[1]:15} {row[2]:15}')
   
    # Commit the changes.
    conn.commit()
    
    # Close the connection.
    conn.close()

# Execute the main function.
main()