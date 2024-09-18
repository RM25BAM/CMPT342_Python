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
if __name__ == '__main__':
    main()