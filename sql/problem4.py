import sqlite3

def add_student(sid, sname, sDept):
    conn = None
    try:
        conn = sqlite3.connect('test.db')
        cur = conn.cursor()
        cur.execute('''INSERT INTO Student
                    (StudentID, StudentName, StudentDept)
                    VALUES (?, ?, ?)''', (sid, sname, sDept))
        conn.commit()

    except sqlite3.Error as err:
        print(err)

    finally:
        if conn != None:
            conn.close()

def create_student_table():
    conn = None
    try:
        conn = sqlite3.connect('test.db')
        cur = conn.cursor()
        cur.execute("DROP TABLE IF EXISTS Student")
    
        # Create the table, if it doesn't already exist.
        cur.execute('''CREATE TABLE IF NOT EXISTS Student (StudentID INTEGER NOT NULL,
                                                          StudentName TEXT,
                                                          StudentDept TEXT,
                                                          PRIMARY KEY (StudentID))''')
        conn.commit()

    except sqlite3.Error as err:
        print(err)

    finally:
        if conn != None:
            conn.close()

def get_info():
    conn = None
    try:
        conn = sqlite3.connect('test.db')
        cur = conn.cursor()
        
        # Select data from the table.
        cur.execute('SELECT * FROM Student')

        # Fetch the results of the SELECT statement.
        results = cur.fetchall()
        return results

    except sqlite3.Error as err:
        print(err)

    finally:
        if conn != None:
            conn.close()
            
def main():
    create_student_table()
    while True:
        sid = input('Enter studentID: ')
        sname = input('Enter student name: ')
        sDept = input('Enter student department: ')
        add_student(sid, sname, sDept)
        inputstud = input('Add another student (y/n): ').lower()
        if (inputstud == 'n' ):
            print('\n Students Info')
            print('---------------------------------')
            for sid, sname, sDept in get_info():
                print(f"ID: {sid}     Name: {sname}      Dept: {sDept}")
            print('\n')
            break
        else:
            continue
    
main()