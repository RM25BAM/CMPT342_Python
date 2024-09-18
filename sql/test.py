import sqlite3

def main():
    # Connect to the database.
    conn = sqlite3.connect('test.db')
    
    # Get a cursor.
    cur = conn.cursor()

    cur.execute('PRAGMA foreign_keys=ON')

    cur.execute("DROP TABLE IF EXISTS Student")
    cur.execute("DROP TABLE IF EXISTS Department")
    
    # Create the table, if it doesn't already exist.
    cur.execute('''CREATE TABLE IF NOT EXISTS Department (DeptName TEXT NOT NULL,
                                                          Location TEXT,
                                                          PRIMARY KEY (DeptName))''')

    # Add two rows to the table.
    cur.execute('''INSERT INTO Department VALUES
                    ("CS", "RLC"), ("BIO", "LEO")''')   

    # Create the table, if it doesn't already exist.
    cur.execute('''CREATE TABLE IF NOT EXISTS Student (StudentID INTEGER NOT NULL,
                                                      StudentName TEXT,
                                                      StudentDept TEXT,
                                                      PRIMARY KEY (StudentID),
                                                      FOREIGN KEY (StudentDept)
                                                      REFERENCES Department(DeptName))''')

    # Add two rows to the table.
    cur.execute('''INSERT INTO Student VALUES
                (1, "Jane Doe", "CS"), (2, "John Doe", "BIO")''')
    
    # Ask user for Student ID.
    sID = int(input('Enter student ID to locate their information: '))
    
    # Select data from the table.
    cur.execute('''SELECT studentName, studentDept, Location
                FROM STUDENT, DEPARTMENT
                WHERE DeptName = StudentDept and studentID = ?''', (sID,))
                # Single element tuple ends with a comma

    # Fetch the results of the SELECT statement.
    results = cur.fetchall()

    # Display the output
    if not results: # Empty lists are false
      print('No student found in the database')
    else:    
      # Display the results.
      for row in results:
          print('Name: ', row[0])
          print('Department: ', row[1])
          print('Location: ', row[2])

    # Commit the changes.
    conn.commit()
    
    # Close the connection.
    conn.close()

# Execute the main function.
if __name__ == '__main__':
    main()
